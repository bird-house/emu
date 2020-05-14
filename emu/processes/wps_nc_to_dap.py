from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS
from pywps.app.Common import Metadata
from pywps import configuration
import logging


LOGGER = logging.getLogger("PYWPS")

# This needs some more thoughts before going live to decide how the WPS server should be configured to communicate
# with the DAP server.


class NcToDap(Process):
    def __init__(self):
        inputs = [
            ComplexInput('resource', "NetCDF file",
                         abstract="Link to NetCDF or NcML file on this server",
                         supported_formats=[FORMATS.NETCDF, ],  # FORMATS.NCML], to become available in PyWPS 4.2.5
                         min_occurs=1,
                         max_occurs=1)
        ]
        outputs = [
            ComplexOutput('dap', 'DAP url',
                          as_reference=True,
                          supported_formats=[FORMATS.DODS]),
        ]

        super(NcToDap, self).__init__(
            self._handler,
            identifier='nc_to_dap',
            title="Convert file URL to DAP URL",
            abstract="Return Data Access Protocol link to a netCDF or NcML file.",
            version="1",
            metadata=[
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    @staticmethod
    def _handler(self, request, response):
        url = request.inputs['resource'][0].url

        # Write response
        file_server = configuration.CONFIG.get("server", "outputurl")
        dap_server = configuration.CONFIG.get("dap", "outputurl")

        response.outputs["dap"].url = url.replace(file_server, dap_server)

        return response
