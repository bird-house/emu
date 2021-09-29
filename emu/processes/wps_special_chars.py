from pywps import Process, LiteralInput, LiteralOutput


class SpecialChars(Process):
    """A process showing the encoding of special characters."""
    def __init__(self):
        inputs = [
            LiteralInput('frost_days', 'Frost Days',
                         abstract='Maximum number of consecutive frost days (Tn < 0).',
                         data_type='integer')]
        outputs = [
            LiteralOutput('output', 'Output response',
                          data_type='string')]

        super(SpecialChars, self).__init__(
            self._handler,
            identifier='special_chars',
            title='<Examples with special charaters>',
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)
        response.outputs['output'].data = 'Frost days: ' + request.inputs['frost_days'][0].data
        response.update_status('PyWPS Process completed.', 100)
        return response
