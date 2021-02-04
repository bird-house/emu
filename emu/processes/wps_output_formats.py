"""
Process returning a variety of output file formats to help test clients.

Author: David Huard
"""
import logging
from pathlib import Path

from pywps import FORMATS, ComplexOutput, Process

LOGGER = logging.getLogger("PYWPS")

# TODO: can be replaced by eggshell function.
DATA_DIR = Path(__file__).parent.parent.joinpath('data')


class OutputFormats(Process):
    def __init__(self):
        inputs = list()
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
            abstract="Dummy process returning various output file formats. Output format "
                     "can be specified between supported formats",
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
            netcdf_out.file = DATA_DIR.joinpath('dummy_nc.zip')
        else:
            netcdf_out.file = DATA_DIR.joinpath('dummy.nc')

        json_out = response.outputs['json']
        if json_out.data_format.mime_type == FORMATS.ZIP.mime_type:
            json_out.file = DATA_DIR.joinpath('dummy_json.zip')
        else:
            json_out.file = DATA_DIR.joinpath('dummy.json')

        response.update_status('PyWPS Process completed.', 100)
        return response
