import os
from pywps import Process, LiteralInput, ComplexOutput
from pywps import FORMATS
from pywps.app.Common import Metadata
from pywps.inout.outputs import FileStorage
import json

import logging
LOGGER = logging.getLogger("PYWPS")


class MultipleOutputs(Process):
    def __init__(self):
        inputs = [
            LiteralInput('count', 'Number of output files',
                         abstract='The number of generated output files.',
                         data_type='integer',
                         default='2',
                         allowed_values=[1, 2, 5, 10])]
        outputs = [
            ComplexOutput('output', 'METALINK output',
                          abstract='Testing metalink output',
                          as_reference=True,
                          supported_formats=[FORMATS.METALINK])
        ]

        super(MultipleOutputs, self).__init__(
            self._handler,
            identifier='multiple_outputs',
            title='Multiple Outputs',
            abstract='Produces multiple files and returns a document'
                     ' with references to these files.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
            ],
            version='1.1',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.info("starting ...")
        if 'count' in request.inputs:
            max_outputs = request.inputs['count'][0].data
        else:
            max_outputs = 2
        # generate outputs
        for i in range(max_outputs):
            # with open(os.path.join(self.workdir, "output_{}.txt".format(i)), 'w') as fp:
            #    fp.write("my output file number %s" % i)
            # response.outputs['output']['out_{}'.format(i)].file = fp.name
            response.outputs['output']['out_{}'.format(i)].data = 'output {}'.format(i)

        response.update_status('PyWPS Process completed.', 100)
        return response
