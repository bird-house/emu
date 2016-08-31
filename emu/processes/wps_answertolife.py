from pywps import Process, LiteralInput, LiteralOutput

import logging


class UltimateQuestionProcess(Process):
    """
    The ultimate process to test the status and update capabilities of the
    server. The processes should be requested as follows:

    ../wps.py?request=execute
    &service=wps
    &version=1.0.0
    &identifier=ultimatequestionprocess
    &status=true
    &storeExecuteResponse=true

    Done by Jorge de Jesus (jmdj@pml.ac.uk) as suggested by Kor de Jong
    """
    def __init__(self):
        inputs = [
            LiteralInput(
                identifier='delay',
                title='Delay between every update',
                abstract='Delay in Seconds. Default: 1 second',
                default='1.0',
                data_type='float')]
        outputs = [
            LiteralOutput(
                identifier='output',
                title='The numerical answer to Life, Universe and Everything',
                data_type='string')]

        # init process
        super(UltimateQuestionProcess, self).__init__(
            self._handler,
            identifier='ultimatequestionprocess',
            version='3.0',
            title='Answer to Life, the Universe and Everything',
            abstract="Numerical solution that is the answer to Life, Universe and Everything. The process is an improvement to Deep Tought computer (therefore version 2.0) since it no longer takes 7.5 milion years, but only a few seconds to give a response, with an update of status every 10 seconds.",
            profile='',
            metadata=['Sleep', 'Wait', 'Delay'],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
            )

    def _handler(self, request, response):
        import time
        sleep_delay = request.inputs['delay'][0].data or 1
        response.update_status('PyWPS Process started. Waiting...', 0)
        for i in range(1, 11):
            time.sleep(sleep_delay)
            response.update_status('Thinking...', i*10)
            logging.info('doing something')
        #The final answer
        response.outputs['output'].data = '42'
        logging.info('final answer')
        return response
