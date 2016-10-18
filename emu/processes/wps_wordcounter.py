import re
from collections import Counter

from pywps import Process, ComplexInput, ComplexOutput, Format, FORMATS

import logging
LOGGER = logging.getLogger("PYWPS")


class WordCounter(Process):
    def __init__(self):
        inputs = [
            ComplexInput('text', 'Text document',
                         abstract='URL pointing to text document',
                         supported_formats=[Format('text/plain')]), ]
        outputs = [
            ComplexOutput('output', 'Word counter result',
                          as_reference=True,
                          supported_formats=[Format('application/json')]), ]

        super(WordCounter, self).__init__(
            self._handler,
            identifier='wordcounter',
            title='Word Counter',
            abstract="Counts words in a given text.",
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line):
                    yield word

        counts = Counter(words(request.inputs['text'][0].stream))
        sorted_counts = sorted([(v, k) for (k, v) in counts.items()],
                               reverse=True)
        with open('out.txt', 'w') as fout:
            fout.write(str(sorted_counts))
            response.outputs['output'].output_format = FORMATS.JSON
            response.outputs['output'].file = fout.name
        return response
