from pywps import Process, LiteralInput
from pywps.app.Common import Metadata
from pywps.app.exceptions import ProcessError

import logging
LOGGER = logging.getLogger("PYWPS")


class ShowError(Process):
    def __init__(self):
        inputs = [
            LiteralInput('message', 'Error Message', data_type='string',
                         abstract='Enter an error message that will be returned.',
                         default="This process failed intentionally.",
                         min_occurs=1,),
            LiteralInput('be_nice', 'Be nice and show a friendly error message. Default: true',
                         data_type='boolean',
                         default=True, ),
        ]

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

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.info("wps_error started ...")
        if request.inputs['be_nice'][0].data is True:
            raise ProcessError(request.inputs['message'][0].data)
        else:
            raise Exception("Sorry, we have no explanation for this error.")
