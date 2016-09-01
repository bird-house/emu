from pywps import Process
from pywps import LiteralInput, LiteralOutput
from pywps import ComplexInput, ComplexOutput
from pywps import Format, FORMATS

import logging
LOGGER = logging.getLogger("PYWPS")


class InOut(Process):
    """
    This process defines several types of literal type of in- and outputs.

    TODO: add literal input with value range[(0,100)] ... see pywps doc
    """

    def __init__(self):
        inputs = [
            LiteralInput('string', 'String', data_type='string',
                         default="This is just a string"),
            LiteralInput('int', 'Integer', data_type='integer',
                         default="7"),
            LiteralInput('float', 'Float', data_type='float',
                         default="3.14"),
            LiteralInput('boolean', 'Boolean', data_type='boolean',
                         default='True'),
            #LiteralInput('time', 'Time', data_type='time'),
            LiteralInput('string_choice', 'String Choice', data_type='string',
                         allowed_values=['one', 'two', 'three'],
                         default='two'),
            ComplexInput('text', 'Text',
                         supported_formats=[Format('text/plain')])


        ]
        outputs = [
            LiteralOutput('string', 'String', data_type='string'),
            LiteralOutput('int', 'Integer', data_type='integer'),
            LiteralOutput('float', 'Float', data_type='float'),
            LiteralOutput('boolean', 'Boolean', data_type='boolean'),
            LiteralOutput('time', 'Time', data_type='time'),
            LiteralOutput('string_choice', 'String Choice', data_type='string'),
            ComplexOutput('text', 'Text',
                          as_reference=True,
                          supported_formats=[Format('text/plain')]),
        ]

        super(InOut, self).__init__(
            self._handler,
            identifier="inout",
            title="InOut",
            version="1.0",
            abstract="Testing all WPS input and output parameters.",
            inputs=inputs,
            outputs=outputs,
            status_supported=True,
            store_supported=True
            )

    def _handler(self, request, response):
        response.outputs['string'].data = request.inputs['string'][0].data
        response.outputs['int'].data = request.inputs['int'][0].data
        response.outputs['float'].data = request.inputs['float'][0].data
        response.outputs['boolean'].data = request.inputs['boolean'][0].data
        response.outputs['string_choice'].data = request.inputs['string_choice'][0].data
        response.outputs['text'].output_format = FORMATS.TEXT
        response.outputs['text'].data = request.inputs['text'][0].data
        return response
