from pywps import Process, LiteralInput, LiteralOutput
from pywps.app.Common import Metadata


class Nap(Process):
    def __init__(self):
        inputs = [
            LiteralInput('delay', 'Delay between every update',
                         default='1', data_type='float')
        ]
        outputs = [
            LiteralOutput('output', 'Nap Output', data_type='string')
        ]

        super(Nap, self).__init__(
            self._handler,
            identifier='nap',
            version='1.0',
            title='Afternoon Nap (supports sync calls only)',
            abstract='This process will have a short nap for a given delay or 1 second if not a valid value.\
                This procces only supports synchronous WPS requests ... \
                so, make sure the nap does not take to long.',
            profile='',
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/')],
            inputs=inputs,
            outputs=outputs,
            store_supported=False,
            status_supported=False
        )

    def _handler(self, request, response):
        import time

        nap_delay = request.inputs['delay'][0].data
        if nap_delay:
            nap_delay = float(nap_delay)
        else:
            nap_delay = 1

        time.sleep(nap_delay)
        response.update_status('PyWPS Process started. Waiting...', 25)
        time.sleep(nap_delay)
        response.update_status('PyWPS Process started. Waiting...', 50)
        time.sleep(nap_delay)
        response.update_status('PyWPS Process started. Waiting...', 75)
        time.sleep(nap_delay)
        response.outputs['output'].data = 'done sleeping'

        return response
