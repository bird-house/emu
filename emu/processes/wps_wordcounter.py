from pywps import Process, ComplexInput, ComplexOutput, Format, FORMATS

import logging
LOGGER = logging.getLogger("PYWPS")


class WordCounter(Process):
    def __init__(self):
        inputs = [
            ComplexInput('text', 'Text document',
                         abstract='URL pointing to text document',
                         supported_formats=[Format('text/plain')]),
            ]
        outputs = [
            ComplexOutput('output', 'Word counter result',
                          supported_formats=[Format('text/plain')])
            ]

        super(WordCounter, self).__init__(
            self._handler,
            identifier='wordcounter',
            title='Word Counter',
            abstract="Counts words in a given text.",
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
            )

    def _handler(self, request, response):
        import re
        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line):
                    yield word

        fin = request.inputs['text'][0].file
        from collections import Counter
        counts = Counter(words(fin))
        sorted_counts = sorted([(v, k) for (k, v) in counts.items()],
                               reverse=True)
        with open('out.txt', 'w') as fout:
            fout.write(str(sorted_counts))
            response.outputs['output'].output_format = Format('text/plain')
            response.outputs['output'].file = fout.name
        return response
