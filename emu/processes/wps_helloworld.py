from pywps import Process, LiteralInput, LiteralOutput, OGCUNIT, UOM


class HelloWorld(Process):
    def __init__(self):
        inputs = [LiteralInput('name', 'Input name', data_type='string')]
        outputs = [LiteralOutput('output', 'Output response', data_type='string')]

        super(HelloWorld, self).__init__(
            self._handler,
            identifier='helloworld',
            title='Process Say Hello',
            version='1.3',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.outputs['output'].data = 'Hello ' + request.inputs['name'][0].data
        response.outputs['output'].uom = UOM('unity')
        return response
