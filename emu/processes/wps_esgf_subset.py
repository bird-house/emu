import os
import json
import six

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy import config

from netCDF4 import Dataset

from subprocess import check_output, CalledProcessError

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata
from owslib import esgfapi

import logging
LOGGER = logging.getLogger("PYWPS")


def ncdump(dataset):
    '''
    Returns the metadata of the dataset

    Code taken from https://github.com/ioos/compliance-checker-web
    '''

    try:
        output = check_output(['ncdump', '-h', dataset])
        if not isinstance(output, six.string_types):
            output = output.decode('utf-8')
        lines = output.split('\n')
        # replace the filename for safety
        dataset_id = os.path.basename(dataset)  # 'uploaded-file'
        lines[0] = 'netcdf {} {{'.format(dataset_id)
        # decode to ascii
        filtered_lines = ['{}\n'.format(line) for line in lines]
    except Exception as err:
        LOGGER.error("Could not generate ncdump: {}".format(err))
        return "Error: generating ncdump failed"
    return filtered_lines


def plot_preview(filename, variable, title=None, output_dir='.'):
    ds = Dataset(filename)
    timestep = 0
    # values
    values = ds.variables[variable][timestep, :, :]
    lats = ds.variables['lat'][:]
    lons = ds.variables['lon'][:]
    # axxis
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.set_global()
    # plot
    plt.contourf(lons, lats, values, 60, transform=ccrs.PlateCarree())
    # Save the plot by calling plt.savefig() BEFORE plt.show()
    plot_name = os.path.basename(filename)
    title = title or plot_name
    output = os.path.join(output_dir, plot_name[:-3] + ".png")
    plt.title(title)
    plt.savefig(output)
    plt.show()
    plt.close()
    return output


def esgf_api(F):
    inputs = [
        ComplexInput('variable', 'variable',
                     abstract="",
                     supported_formats=[FORMATS.JSON],
                     min_occurs=0, max_occurs=1,
                     mode=MODE.SIMPLE
                     ),
        ComplexInput('domain', 'domain',
                     abstract="",
                     supported_formats=[FORMATS.JSON],
                     min_occurs=0, max_occurs=1,
                     mode=MODE.SIMPLE
                     ),
        ComplexInput('operation', 'operation',
                     abstract="",
                     supported_formats=[FORMATS.JSON],
                     min_occurs=0, max_occurs=1,
                     mode=MODE.SIMPLE
                     ),
    ]

    def wrapper(self):
        F(self)
        self.profile.append('ESGF-API')
        self.inputs.extend(inputs)
    return wrapper


class EmuSubset(Process):
    """
    Notes
    -----

    subset netcdf files
    """
    @esgf_api
    def __init__(self):
        inputs = []
        outputs = [
            ComplexOutput('output', 'Output',
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF], ),
            ComplexOutput('ncdump', 'Metadata',
                          abstract='ncdump of subsetted Dataset.',
                          as_reference=True,
                          supported_formats=[FORMATS.TEXT], ),
            ComplexOutput('preview', 'Preview',
                          abstract='Preview of subsetted Dataset.',
                          as_reference=True,
                          supported_formats=[Format('image/png')],), ]
        super(EmuSubset, self).__init__(
            self._handler,
            identifier='emu_subset',
            title='xarray.subset',
            abstract="subset netcdf files",
            version='1',
            metadata=[
                Metadata('ESGF Compute API', 'https://github.com/ESGF/esgf-compute-api'),
                Metadata('ESGF Compute WPS', 'https://github.com/ESGF/esgf-compute-wps'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        # TODO: handle api_key in pywps or twitcher middleware
        # api_key = request.http_request.headers.get('Api-Key')

        # subsetting
        import xarray as xr
        response.update_status('PyWPS Process started.', 0)

        variable = esgfapi.Variable.from_json(json.loads(request.inputs['variable'][0].data))
        domain = esgfapi.Domain.from_json(json.loads(request.inputs['domain'][0].data))

        # TODO: Use chunks for parallel processing with dask.distributed
        output_file = self.workdir + '/out.nc'
        with xr.open_dataset(variable.uri) as ds:
            da = ds[variable.var_name]
            sl = {}
            for dim in domain.dimensions:
                sl = {dim['name']: slice(dim['start'], dim['end'], dim['step'])}
                if dim['crs'] == 'values':
                    da = da.sel(**sl)
                elif dim['crs'] == 'indices':
                    da = da.isel(**sl)
            if 0 in da.shape:
                raise ValueError("Subsetting operation yields no values for `{}` dimension.".
                                 format(da.dims[da.shape.index(0)]))

            da.to_netcdf(output_file)
        response.outputs['output'].file = output_file
        response.update_status('subsetting done.', 70)
        # plot preview
        try:
            # TODO: regrid outpuf file before plotting
            #response.outputs['preview'].file = plot_preview(
            #    output_file, title="Test", variable=variable.var_name,
            #    output_dir=self.workdir)
            response.outputs['preview'].file = self.simple_plot_preview(da)
            response.update_status('plot done.', 80)
        except Exception:
            response.outputs['preview'].data = 'plot failed'
            response.update_status('plot failed.', 80)
        # run ncdump
        with open(os.path.join(self.workdir, "nc_dump.txt"), 'w') as fp:
            fp.writelines(ncdump(output_file))
        response.outputs['ncdump'].file = fp.name
        response.update_status('ncdump done.', 90)
        # done
        response.update_status('PyWPS Process completed.', 100)
        return response

    def simple_plot_preview(self, da):
        """Plot map of first time step."""
        fig, ax = plt.subplots(1, 1)
        da.isel(time=0).plot(ax=ax)
        fn = os.path.join(self.workdir, 'preview.png')
        fig.savefig(fn)
        plt.close()
        return fn
