# -*- encoding: utf-8 -*-
"""
Dummy process with non-pythonic identifiers.

"""
from pywps import Process, LiteralInput, LiteralOutput, ComplexInput, ComplexOutput, FORMATS

import logging
LOGGER = logging.getLogger("PYWPS")


class NonPyID(Process):
    def __init__(self):
        inputs = [
            LiteralInput('input 1', 'Input1 number',
                         default='100', data_type='integer'),
            ComplexInput('input-2', 'json input',
                         supported_formats=[FORMATS.JSON, ]),
        ]
        outputs = [
            LiteralOutput('output.1', 'Add 1 to `input 1`.',
                          data_type='float'),
            ComplexOutput('output 2', 'Same thing as input-2.',
                          supported_formats=[FORMATS.JSON, ]),
        ]

        super(NonPyID, self).__init__(
            self._handler,
            identifier='non.py-id',  # TODO:fails with pywps: u'fake.process-for testing &é;'
            title="Dummy process including non-pythonic identifiers",
            abstract="Dummy process whose process, input and output identifiers include characters not allowed "
                     "in Python.",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.debug("input1 %s", request.inputs['input 1'][0].data)
        LOGGER.debug("input2 %s", request.inputs['input-2'][0].data)
        response.outputs['output.1'].data = request.inputs['input 1'][0].data + 1
        response.outputs['output 2'].data = request.inputs['input-2'][0].data

        response.update_status('PyWPS Process completed.', 100)
        return response
