import os
import json

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

        super(CDATSubset, self).__init__(
            self._handler,
            identifier='CDAT.subset',
            title='CDAT.subset',
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
        response.update_status('PyWPS Process started.', 0)
        data = {}
        output = {'output': data}
        for param in ['variable', 'domain', 'operation']:
            if param in request.inputs:
                data[param] = json.loads(request.inputs[param][0].data)
        response.outputs['output'].data = json.dumps(output)
        response.update_status('PyWPS Process completed.', 100)
        return response
