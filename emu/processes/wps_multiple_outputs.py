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
                         abstract='The number of generated output files.',
                         data_type='integer',
                         default='1',
                         allowed_values=[1, 2, 5, 10])]
        outputs = [
            ComplexOutput('output', 'Output',
                          abstract='Text document with dummy content.',
                          as_reference=True,
                          supported_formats=[Format('text/plain')]),
            ComplexOutput('reference', 'Output References',
                          abstract='Document with references to produced output files.',
                          as_reference=True,
                          supported_formats=[Format('application/json')]), ]

        super(MultipleOutputs, self).__init__(
            self._handler,
            identifier='multiple_outputs',
            title='Multiple Outputs',
            abstract='Produces multiple files and returns a document'
                     ' with references to these files.',
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
        # prepare output
        response.outputs['output'].storage = FileStorage()
        response.outputs['output'].output_format = FORMATS.TEXT
        # generate outputs
        result = dict(count=max_outputs, outputs=[])
        for i in range(max_outputs):
            progress = int(i * 100.0 / max_outputs)
            response.update_status('working on document {}'.format(i), progress)
            response.outputs['output'].data = "output file number {}".format(i)
            ref_url = response.outputs['output'].get_url()
            result['outputs'].append(dict(name=os.path.basename(ref_url), url=ref_url))
        # return document with outpus
        response.outputs['reference'].output_format = FORMATS.JSON
        response.outputs['reference'].data = json.dumps(result)
        return response
