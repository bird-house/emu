from pywps import Process, LiteralInput, LiteralOutput
from pywps.app.Common import Metadata


class Sleep(Process):
    """A long running process, just sleeping."""
    def __init__(self):
        inputs = [
            LiteralInput('delay', 'Delay between every update',
                         default='2', data_type='float')
        ]
        outputs = [
            LiteralOutput('sleep_output', 'Sleep Output', data_type='string')
        ]

        super(Sleep, self).__init__(
            self._handler,
            identifier='sleep',
            version='1.0',
            title='Sleep Process',
            abstract='Testing a long running process, in the sleep.'
                     'This process will sleep for a given delay or 10 seconds if not a valid value.',
            profile='',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
                Metadata('PyWPS Demo', 'https://pywps-demo.readthedocs.io/en/latest/'),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        import time

        if 'delay' in request.inputs:
            sleep_delay = request.inputs['delay'][0].data
        else:
            sleep_delay = 2

        response.update_status('PyWPS Process started. Waiting...', 0)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 20)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 40)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 60)
        time.sleep(sleep_delay)
        response.update_status('PyWPS Process started. Waiting...', 80)
        time.sleep(sleep_delay)
        response.outputs['sleep_output'].data = 'done sleeping'

        response.update_status('PyWPS Process completed.', 100)
        return response
