import os
import json

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata
from owslib import esgfapi
import logging
LOGGER = logging.getLogger("PYWPS")


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
                          mode=MODE.SIMPLE), ]

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
        with xr.open_dataset(variable.uri) as ds:
            da = ds[variable.var_name]
            sl = {}
            for dim in domain.dimensions:
                sl = {dim['name']: slice(dim['start'], dim['end'], dim['step'])}
                if dim['crs'] == 'values':
                    da = da.sel(**sl)
                elif dim['crs'] == 'indices':
                    da = da.isel(**sl)

            da.to_netcdf(self.workdir + '/out.nc')

        response.outputs['output'].file = self.workdir + '/out.nc'
        response.update_status('PyWPS Process completed.', 100)
        return response
