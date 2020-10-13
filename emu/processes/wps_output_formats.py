"""
Process returning a variety of output file formats to help test clients.

Author: David Huard
"""
import os
from pywps import Process, ComplexOutput
from pywps import FORMATS

import logging
LOGGER = logging.getLogger("PYWPS")

# TODO: can be replaced by eggshell function.
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class OutputFormats(Process):
    def __init__(self):
        inputs = []
        outputs = [
            ComplexOutput('netcdf', 'netCDF dummy output file.',
                          abstract="A very small test netCDF file. ",
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF, FORMATS.ZIP]),
            ComplexOutput('json', 'json dummy output file.',
                          abstract="A very small test json file. ",
                          as_reference=False,
                          supported_formats=[FORMATS.JSON, FORMATS.ZIP, FORMATS.TEXT]),
        ]

        super(OutputFormats, self).__init__(
            self._handler,
            identifier='output_formats',
            title="Return different output formats.",
            abstract="Dummy process returning various output file formats. Output format can be specified between supported formats",
            version="2.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        netcdf_out = response.outputs['netcdf']
        if netcdf_out.data_format.mime_type == FORMATS.ZIP.mime_type:
            netcdf_out.file = os.path.join(DATA_DIR, 'dummy_nc.zip')
        else:
            netcdf_out.file = os.path.join(DATA_DIR, 'dummy.nc')

        json_out = response.outputs['json']
        if json_out.data_format.mime_type == FORMATS.ZIP.mime_type:
            json_out.file = os.path.join(DATA_DIR, 'dummy_json.zip')
        else:
            json_out.file = os.path.join(DATA_DIR, 'dummy.json')

        response.update_status('PyWPS Process completed.', 100)
        return response
