"""
Process returning a variety of output file formats to help test clients.

Author: David Huard
"""
import os
from pywps import Process, ComplexOutput
from pywps import FORMATS
from eggshell.config import Paths
import emu
import logging
LOGGER = logging.getLogger("PYWPS")
paths = Paths(emu)


class OutputFormats(Process):
    def __init__(self):
        inputs = []
        outputs = [
            ComplexOutput('netcdf', 'netCDF dummy output file.',
                          abstract="A very small test netCDF file. ",
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF, ]),
            ComplexOutput('json', 'json dummy output file.',
                          abstract="A very small test json file. ",
                          as_reference=False,
                          supported_formats=[FORMATS.JSON, ]),
        ]

        super(OutputFormats, self).__init__(
            self._handler,
            identifier='output_formats',
            title="Return different output formats. ",
            abstract="Dummy process returning various output file formats.",
            version="2.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        response.outputs['netcdf'].file = os.path.join(paths.data, 'dummy.nc')
        response.outputs['json'].file = os.path.join(paths.data, 'dummy.json')

        response.update_status('PyWPS Process completed.', 100)
        return response
