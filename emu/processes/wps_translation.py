"""
Translation process to check WPS translations
"""
from pywps import Process, LiteralInput, LiteralOutput

import logging
LOGGER = logging.getLogger("PYWPS")


class Translation(Process):
    def __init__(self):
        inputs = [
            LiteralInput('input1', 'Input1 number',
                         default='100', data_type='integer',
                         translations={"fr-CA": {"title": "Entrée #1", "abstract": "Entier #1"}}),
        ]
        outputs = [
            LiteralOutput('output1', 'Output1 add 1 result',
                          data_type='string',
                          translations={"fr-CA": {"title": "Sortie #1", "abstract": "Chaîne de charactères"}}),
        ]

        super(Translation, self).__init__(
            self._handler,
            identifier='translation',
            title="Translated process",
            abstract="Process including translations in other languages.",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
            keywords=["languages"],
            translations={"fr-CA": {"title": "Processus traduit", "abstract": "Processus incluant des traductions",
                                    "keywords": ["langues"]}}
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.debug("input1 %s", request.inputs['input1'][0].data)
        response.outputs['output1'].data = request.inputs['input1'][0].data + 1

        response.update_status('PyWPS Process completed.', 100)
        return response
