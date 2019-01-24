import os
import json

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy import config

from netCDF4 import Dataset

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata
from owslib import esgfapi
import logging
LOGGER = logging.getLogger("PYWPS")


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


class EmuSubset(Process):
    """
    Notes
    -----

    subset netcdf files
    """
    def __init__(self):
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
        outputs = [
            ComplexOutput('output', 'Output',
                          as_reference=True,
                          supported_formats=[FORMATS.JSON],
                          mode=MODE.SIMPLE),
            ComplexOutput('preview', 'Preview',
                          abstract='Preview of subsetted Dataset.',
                          as_reference=True,
                          supported_formats=[Format('image/png')]), ]
        super(EmuSubset, self).__init__(
            self._handler,
            identifier='Emu.subset',
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
            da.to_netcdf(output_file)
        response.outputs['output'].file = output_file
        response.update_status('subsetting done.', 70)
        # plot preview
        try:
            response.outputs['preview'].file = plot_preview(
                output_file, title="Test", variable=variable.var_name,
                output_dir=self.workdir)
            response.update_status('plot done.', 80)
        except Exception:
            response.outputs['preview'].data = 'plot failed'
            response.update_status('plot failed.', 80)
        # done
        response.update_status('PyWPS Process completed.', 100)
        return response
