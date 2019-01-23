import os

from pywps import Process
from pywps import ComplexInput, ComplexOutput, FORMATS, Format
from pywps.inout.basic import SOURCE_TYPE
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")


class CDATSubset(Process):
    """
    Notes
    -----

    subset netcdf files
    """
    def __init__(self):
        inputs = [
            ComplexInput('variable', 'Variable',
                         abstract="",
                         supported_formats=[FORMATS.JSON],
                         min_occurs=0, max_occurs=1,
                         # mode=MODE.STRICT
                         ),
        ]
        outputs = [
            ComplexOutput('output', 'Output',
                          as_reference=True,
                          supported_formats=[FORMATS.TEXT]), ]

        super(CDATSubset, self).__init__(
            self._handler,
            identifier='CDAT.subset',
            title='CDAT.subset',
            abstract="",
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
        response.update_status('PyWPS Process started.', 0)
        response.outputs['output'].data = request.inputs['variable'][0].data
        response.update_status('PyWPS Process completed.', 100)
        return response
