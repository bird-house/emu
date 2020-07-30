import os
from pywps import Process, LiteralInput, ComplexOutput
from pywps import FORMATS
from pywps.inout.literaltypes import AllowedValue
from pywps.ext_autodoc import MetadataUrl
from pywps.inout.outputs import MetaLink, MetaLink4, MetaFile
import json

import logging
LOGGER = logging.getLogger("PYWPS")


class MultipleOutputs(Process):
    def __init__(self):
        inputs = [
            LiteralInput('count', 'Number of output files',
                         abstract='The number of generated output files.',
                         data_type='integer',
                         default=2,
                         allowed_values=[AllowedValue(minval=1, maxval=10)])]
        outputs = [
            ComplexOutput('output', 'METALINK v3 output',
                          abstract='Testing metalink v3 output',
                          as_reference=True,
                          supported_formats=[FORMATS.METALINK]),
            ComplexOutput('output_meta4', 'METALINK v4 output',
                          abstract='Testing metalink v4 output',
                          as_reference=True,
                          supported_formats=[FORMATS.META4])
        ]

        super(MultipleOutputs, self).__init__(
            self._handler,
            identifier='multiple_outputs',
            title='Multiple Outputs',
            abstract='Produces multiple files and returns a document'
                     ' with references to these files.',
            metadata=[
                MetadataUrl('User Guide',
                            'https://emu.readthedocs.io/en/latest/processes.html',
                            anonymous=True),
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
        max_outputs = request.inputs['count'][0].data

        # generate MetaLink v3 output
        ml3 = MetaLink('test-ml-1', 'Testing MetaLink with text files.', workdir=self.workdir)
        for i in range(max_outputs):
            mf = MetaFile('output_{}'.format(i), 'Test output', fmt=FORMATS.TEXT)
            mf.data = 'output: {}'.format(i)
            ml3.append(mf)
        response.outputs['output'].data = ml3.xml

        # ... OR generate MetaLink v4 output (recommended)
        ml4 = MetaLink4('test-ml-1', 'Testing MetaLink with text files.', workdir=self.workdir)
        for i in range(max_outputs):
            mf = MetaFile('output_{}'.format(i), 'Test output', fmt=FORMATS.TEXT)
            mf.data = 'output: {}'.format(i)
            ml4.append(mf)
        response.outputs['output_meta4'].data = ml4.xml

        response.update_status('PyWPS Process completed.', 100)
        return response
