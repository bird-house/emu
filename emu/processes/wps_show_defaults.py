from pywps import Process, LiteralInput, LiteralOutput

import logging
LOGGER = logging.getLogger("PYWPS")


class ShowDefaults(Process):
    """
    Process with examples of default value usage in WPS.
    """
    def __init__(self):
        inputs = [
            LiteralInput(
                'string_1',
                'String 1',
                data_type='string',
                default='one',
                min_occurs=0
            ),
            LiteralInput(
                'string_2',
                'String 2',
                data_type='string',
                default='two',
                min_occurs=1
            ),
            LiteralInput(
                'string_3',
                'String 3',
                data_type='string',
                # default='three',
                min_occurs=1
            ),
        ]
        outputs = [
            LiteralOutput(
                'output',
                'Output',
                data_type='string',
            ),
        ]

        super(ShowDefaults, self).__init__(
            self._handler,
            identifier='show_defaults',
            title="Show defaults",
            abstract="Show usage of default values in WPS",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        response.outputs['output'].data = f"""
        Outputs:
        string1={request.inputs['string_1'][0].data},
        string2={request.inputs['string_2'][0].data},
        string3={request.inputs['string_3'][0].data}
        """

        response.update_status('PyWPS Process completed.', 100)
        return response
