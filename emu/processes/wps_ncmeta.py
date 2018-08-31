import os

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata

from netCDF4 import Dataset

import logging
LOGGER = logging.getLogger("PYWPS")


TEST_URL = 'http://test.opendap.org:80/opendap/netcdf/examples/sresa1b_ncar_ccsm3_0_run1_200001.nc'


class NCMeta(Process):
    """
    Notes
    -----

    Returns metadata of a NetCDF file or OpenDAP resource.
    """
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'NetCDF Dataset',
                         abstract="{}.nc4".format(TEST_URL),
                         # default="{}.nc4".format(TEST_URL),
                         supported_formats=[FORMATS.NETCDF],
                         min_occurs=0, max_occurs=1,
                         # default_type=SOURCE_TYPE.URL,
                         mode=MODE.STRICT),

            ComplexInput('dataset_opendap', 'OpenDAP Dataset',
                         abstract=TEST_URL,
                         # default=TEST_URL,
                         supported_formats=[FORMATS.DODS],
                         min_occurs=0, max_occurs=1,
                         # default_type=SOURCE_TYPE.URL,
                         mode=MODE.STRICT),
        ]
        outputs = [
            ComplexOutput('output', 'Metadata',
                          as_reference=True,
                          supported_formats=[FORMATS.TEXT]), ]

        super(NCMeta, self).__init__(
            self._handler,
            identifier='ncmeta',
            title='Show NetCDF Metadata',
            abstract="Dataset can be either a NetCDF file or an OpenDAP service.",
            version='4',
            metadata=[
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        # TODO: can't set default value for input otherwise I will always get
        # both dataset and dataset_opendap
        if 'dataset_opendap' in request.inputs:
            inpt = request.inputs['dataset_opendap'][0]
            resource = inpt.url
        else:
            inpt = request.inputs['dataset'][0]
            resource = inpt.file
        ds = Dataset(resource)
        with open(os.path.join(self.workdir, 'out.txt'), "w") as fp:
            response.outputs['output'].file = fp.name
            fp.write("URL: {}\n\n".format(inpt.url))
            fp.write("MIME Type: {}\n\n".format(inpt.data_format.mime_type))
            for attr in ds.ncattrs():
                fp.write("{}: {}\n\n".format(attr, ds.getncattr(attr)))
        return response
