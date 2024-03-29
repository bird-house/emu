from pywps import Process, LiteralOutput
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
            abstract='This process gives the answer to the ultimate question of life, the universe, and everything.',
            profile='',
            metadata=[Metadata('Ultimate Question'), Metadata('What is the meaning of life')],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        import time
        sleep_delay = .1
        response.update_status('PyWPS Process started.', 0)
        time.sleep(sleep_delay)

        response.update_status("Contacting the Deep Thought supercomputer.", 10)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 20)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 40)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 60)
        time.sleep(sleep_delay)
        response.update_status('Thinking...', 80)
        response.outputs['answer'].data = '42'

        response.update_status('PyWPS Process completed.', 100)
        return response
