from pywps import Process, LiteralInput
from pywps.app.Common import Metadata

import logging
logger = logging.getLogger("PYWPS")


class ShowError(Process):
    def __init__(self):
        inputs = [
            LiteralInput('message', 'Error Message', data_type='string',
                         abstract='Enter an error message that will be returned.',
                         default="This process failed intentionally :)",
                         min_occurs=1,)]

        super(ShowError, self).__init__(
            self._handler,
            identifier='show_error',
            title='Show a WPS Error',
            abstract='This process will fail intentionally with a WPS error message.',
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/')],
            version='1.0',
            inputs=inputs,
            # outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        logger.info("wps_error started ...")
        raise Exception(request.inputs['message'][0].data)
