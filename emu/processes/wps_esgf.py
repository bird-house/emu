from pywps import Process, LiteralInput, LiteralOutput, UOM
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")


class ESGFDemo(Process):
    def __init__(self):
        inputs = [
            LiteralInput('variable', 'Variable',
                         abstract='Choose a variable.',
                         data_type='string')]
        outputs = [
            LiteralOutput('output', 'Output response',
                          abstract='A summary report.',
                          data_type='string')]

        super(ESGFDemo, self).__init__(
            self._handler,
            identifier='esgf_demo',
            title='ESGF Demo Process',
            abstract='Shows how to use WPS metadata for processes using ESGF data.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
                Metadata('PyWPS Demo', 'https://pywps-demo.readthedocs.io/en/latest/'),
            ],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("starting ...")
        response.outputs['output'].data = 'Variable={0}'.format(request.inputs['variable'][0].data)
        response.update_status('done', 100)
        return response
