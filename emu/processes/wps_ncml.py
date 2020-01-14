import os

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata
from pathlib import Path

from netCDF4 import Dataset

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
                          supported_formats=[FORMATS.TEXT]),
        ]

        super(NcMLAgg, self).__init__(
            self._handler,
            identifier='ncml',
            title="Tets NcML THREDDS capability",
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
        import xarray.tests.test_dataset as td

        d1, d2, d3 = td.create_append_test_data()

        d1fn = Path(self.workdir) / "d1.nc"
        d2fn = Path(self.workdir) / "d2.nc"

        ncml = """
        <netcdf xmlns="http://www.unidata.ucar.edu/namespaces/netcdf/ncml-2.2">
            <aggregation dimName="time" type="joinExisting">
                <scan location="." suffix=".nc" subdirs="false"/>
            </aggregation>
        </netcdf>
        """

        d1.to_netcdf(d1fn)
        d2.to_netcdf(d2fn)

        with open(os.path.join(self.workdir, 'agg.ncml'), "w") as fp:
            response.outputs['ncml'].file = fp.name
            fp.write(ncml)

        return response
