"""
DummyProcess to check the WPS structure

Author: Jorge de Jesus (jorge.jesus@gmail.com) as suggested by Kor de Jong
"""
from pywps import Process, LiteralInput, LiteralOutput

import logging
LOGGER = logging.getLogger("PYWPS")


class Dummy(Process):
    def __init__(self):
        inputs = [
            LiteralInput('input1', 'Input1 number',
                         default='100', data_type='integer'),
            LiteralInput('input2', 'Input2 number',
                         default='200', data_type='integer'),
        ]
        outputs = [
            LiteralOutput('output1', 'Output1 add 1 result',
                          data_type='string'),
            LiteralOutput('output2', 'Output2 substract 1 result',
                          data_type='string'),
        ]

        super(Dummy, self).__init__(
            self._handler,
            identifier='dummyprocess',
            title="Dummy Process",
            version="2.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.debug("input1 %s", request.inputs['input1'][0].data)
        LOGGER.debug("input2 %s", request.inputs['input2'][0].data)
        response.outputs['output1'].data = request.inputs['input1'][0].data + 1
        response.outputs['output2'].data = request.inputs['input2'][0].data - 1
        return response
