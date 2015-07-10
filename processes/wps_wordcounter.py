from malleefowl.process import WPSProcess

from malleefowl import wpslogging as logging
logger = logging.getLogger(__name__)


class WordCountProcess(WPSProcess):
    """
    Counts words in a given text ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="wordcount", 
            title="Word Counter",
            version = "1.0",
            metadata = [],
            abstract="Counts words in a given text ...",
            )

        self.text = self.addComplexInput(
            identifier = "text",
            title = "Text document",
            abstract = "URL of text document",
            metadata=[],
            minOccurs=1,
            maxOccurs=1,
            formats=[{"mimeType":"text/plain"}],
            maxmegabites=2,
            )
        
        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Word count result",
            metadata=[],
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        self.show_status("Starting ...", 1)

        import re
        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line):
                    yield word

        text = self.text.getValue()
        logger.debug('input file = %s', text)
        with open(text, 'r') as fin:
            from collections import Counter
            counts = Counter(words(fin))
            sorted_counts = sorted([(v,k) for (k,v) in counts.items()], reverse=True)
            logger.debug('words counted')
            outfile = self.mktempfile(suffix='.txt')
            with open(outfile, 'w') as fout:
                logger.debug('writing to %s', outfile)
                fout.write( str(sorted_counts) )
                self.output.setValue( fout.name )

        self.show_status("Done", 100)

