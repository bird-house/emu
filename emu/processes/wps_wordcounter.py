from pywps.Process import WPSProcess

class WordCountProcess(WPSProcess):
    """
    Counts words in a given text ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="wordcount", 
            title="Word Counter",
            version="0.3",
            abstract="Counts words in a given text ...",
            statusSupported=True,
            storeSupported=True
            )

        self.text = self.addComplexInput(
            identifier="text",
            title="Text document",
            abstract="URL of text document",
            minOccurs=1,
            maxOccurs=1,
            formats=[{"mimeType":"text/plain"}],
            maxmegabites=2,
            )
        
        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Word count result",
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        import re
        wordre = re.compile(r'\w+')

        def words(f):
            for line in f:
                for word in wordre.findall(line):
                    yield word

        text = self.text.getValue()
        with open(text, 'r') as fin:
            from collections import Counter
            counts = Counter(words(fin))
            sorted_counts = sorted([(v,k) for (k,v) in counts.items()], reverse=True)
            outfile = 'out.txt'
            with open(outfile, 'w') as fout:
                fout.write( str(sorted_counts) )
                self.output.setValue( fout.name )

        self.status.set("Done", 100)

