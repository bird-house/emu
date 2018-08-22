import os

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")

FORMAT_OPENDAP = Format('application/x-ogc-dods')


class NCMeta(Process):
    """
    Notes
    -----

    Returns metadata of a NetCDF file or OpenDAP resource.
    """
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'Dataset',
                         supported_formats=[FORMATS.NETCDF],
                         min_occurs=0,
                         mode=MODE.NONE),
            ComplexInput('dataset_opendap', 'Dataset OpenDAP',
                         supported_formats=[FORMAT_OPENDAP],
                         min_occurs=0,
                         mode=MODE.NONE),
        ]
        outputs = [
            ComplexOutput('output', 'Metadata',
                          as_reference=True,
                          supported_formats=[FORMATS.TEXT]), ]

        super(NCMeta, self).__init__(
            self._handler,
            identifier='ncmeta',
            title='Show NetCDF Metadata',
            version='4',
            metadata=[
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        from netCDF4 import Dataset
        if 'dataset_opendap' in request.inputs:
            inpt = request.inputs['dataset_opendap'][0]
            ds = Dataset(inpt.url)
        else:
            inpt = request.inputs['dataset'][0]
            ds = Dataset(inpt.file)
        with open(os.path.join(self.workdir, 'out.txt'), "w") as fp:
            response.outputs['output'].file = fp.name
            fp.write("URL: {}\n\n".format(inpt.url))
            fp.write("MIME Type: {}\n\n".format(inpt.data_format.mime_type))
            for attr in ds.ncattrs():
                fp.write("{}: {}\n\n".format(attr, ds.getncattr(attr)))
        return response
