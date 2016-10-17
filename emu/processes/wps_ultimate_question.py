from pywps import Process, LiteralInput, LiteralOutput
from pywps.app.Common import Metadata


class UltimateQuestion(Process):
    def __init__(self):
        inputs = []
        outputs = [LiteralOutput('answer', 'Answer to Ultimate Question', data_type='string')]

        super(UltimateQuestion, self).__init__(
            self._handler,
            identifier='ultimate_question',
            version='2.0',
            title='Answer to the ultimate question',
            abstract='This process gives the answer to the ultimate question of "What is the meaning of life?',
            profile='',
            metadata=[Metadata('Ultimate Question'), Metadata('What is the meaning of life')],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        import time
        sleep_delay = 2
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 20)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 40)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 60)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 80)
        response.outputs['answer'].data = '42'
        return response
