import json
import logging
import re
from collections import Counter

from pywps import FORMATS, ComplexInput, ComplexOutput, Process
from pywps.ext_autodoc import MetadataUrl

LOGGER = logging.getLogger("PYWPS")


class WordCounter(Process):
    """
    Notes:

    Counts occurrences of all words in a document.
    """
    def __init__(self):
        inputs = [
            ComplexInput('text', 'Text document',
                         abstract='URL pointing to a text document, for example "Alice in Wonderland":'
                                  ' http://www.gutenberg.org/cache/epub/19033/pg19033.txt',
                         supported_formats=[FORMATS.TEXT]), ]
        outputs = [
            ComplexOutput('output', 'Word counter result',
                          as_reference=True,
                          supported_formats=[FORMATS.JSON]), ]

        super(WordCounter, self).__init__(
            self._handler,
            identifier='wordcounter',
            title='Word Counter',
            abstract="Counts words in a given text.",
            version='1.0',
            metadata=[
                MetadataUrl('User Guide',
                            'http://emu.readthedocs.io/en/latest/',
                            anonymous=True),
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        response.update_status('PyWPS Process started.', 0)

        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line.decode('UTF-8')):
                    yield word

        counts = Counter(words(request.inputs['text'][0].stream))
        sorted_counts = sorted([(v, k) for (k, v) in counts.items()],
                               reverse=True)

        response.outputs['output'].data = json.dumps(sorted_counts)

        response.update_status('PyWPS Process completed.', 100)
        return response
