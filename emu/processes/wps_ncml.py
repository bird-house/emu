import os
import xarray.tests.test_dataset as td
from pywps import Process
from pywps import ComplexOutput, FORMATS
from pywps.app.Common import Metadata
import logging


LOGGER = logging.getLogger("PYWPS")


class NcMLAgg(Process):
    def __init__(self):
        inputs = []
        outputs = [
            ComplexOutput('d1', 'NetCDF file 1',
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF]),
            ComplexOutput('d2', 'NetCDF file 2',
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF]),
            ComplexOutput('ncml', 'NcML aggregation',
                          as_reference=True,
                          supported_formats=[FORMATS.DODS]),  # FORMATS.NCML To become available in PyWPS 4.2.5
        ]

        super(NcMLAgg, self).__init__(
            self._handler,
            identifier='ncml',
            title="Test NcML THREDDS capability",
            abstract="Return links to an NcML file aggregating netCDF files with moving time units.",
            version="1",
            metadata=[
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):

        # Create test datasets
        d1, d2, _ = td.create_append_test_data()

        # Save datasets to disk
        d1fn = os.path.join(self.workdir, "d1.nc")
        d2fn = os.path.join(self.workdir, "d2.nc")

        d1.to_netcdf(d1fn)
        d2.to_netcdf(d2fn)

        # Create NcML aggregation
        ncml = """
        <netcdf xmlns="http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2">
            <aggregation dimName="time" type="joinExisting">
                <scan location="." suffix=".nc" subdirs="false"/>
            </aggregation>
        </netcdf>
        """

        # Write response
        response.outputs["d1"].file = d1fn
        response.outputs["d2"].file = d2fn

        response.outputs['ncml'].data = ncml

        return response
