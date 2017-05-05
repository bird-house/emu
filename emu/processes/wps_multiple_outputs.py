import os
from pywps import Process, LiteralInput, ComplexOutput
from pywps import Format, FORMATS
from pywps.app.Common import Metadata
from pywps.inout.storage import FileStorage
import json

import logging
LOGGER = logging.getLogger("PYWPS")


class MultipleOutputs(Process):
    def __init__(self):
        inputs = [
            LiteralInput('count', 'Number of output files',
                         abstract='The number of output files is flexible.',
                         data_type='integer',
                         default='1',
                         allowed_values=[1, 2, 5, 10])]
        outputs = [
            ComplexOutput('output', 'Output',
                          abstract='Document with references to produced output files.',
                          as_reference=True,
                          supported_formats=[Format('application/json')]), ]

        super(MultipleOutputs, self).__init__(
            self._handler,
            identifier='multiple_outputs',
            title='Multiple Outputs',
            abstract='Produces a multiple output files and returns a document'
                     ' with references to this files.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
            ],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("starting ...")
        if 'count' in request.inputs:
            max_outputs = request.inputs['count'][0].data
        else:
            max_outputs = 1
        # prepare dummy output object
        temp_out = ComplexOutput('_output', 'Temp Output',
                                 as_reference=True,
                                 supported_formats=[Format('text/plain')])
        temp_out.storage = FileStorage()
        temp_out.output_format = FORMATS.TEXT
        # generate outputs
        result = dict(count=max_outputs, outputs=[])
        for i in range(max_outputs):
            temp_out.data = "output files {}".format(i)
            ref_url = temp_out.get_url()
            result['outputs'].append(dict(name=os.path.basename(ref_url), url=ref_url))
        # return document with outpus
        response.outputs['output'].output_format = FORMATS.JSON
        response.outputs['output'].data = json.dumps(result)
        return response
