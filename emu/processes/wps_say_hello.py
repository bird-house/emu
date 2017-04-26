from pywps import Process, LiteralInput, LiteralOutput, UOM

import logging
LOGGER = logging.getLogger("PYWPS")


class SayHello(Process):
    def __init__(self):
        inputs = [
            LiteralInput('name', 'Your name',
                         abstract='Please enter your name.',
                         data_type='string')]
        outputs = [
            LiteralOutput('output', 'Output response',
                          abstract='A friendly Hello from us.',
                          data_type='string')]

        super(SayHello, self).__init__(
            self._handler,
            identifier='hello',
            title='Say Hello',
            abstract='Returns a literal string output with Hello plus the inputed name.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/'),  # noqa
                Metadata('PyWPS Demo', 'https://pywps-demo.readthedocs.io/en/latest/'),
            ],
            version='1.5',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("say hello")
        response.outputs['output'].data = 'Hello ' + request.inputs['name'][0].data
        response.outputs['output'].uom = UOM('unity')
        return response
