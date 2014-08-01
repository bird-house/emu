"""
Processes for testing wps service
"""

from datetime import datetime, date
import types

from malleefowl.process import WPSProcess

from malleefowl import wpslogging as logging
logger = logging.getLogger(__name__)


class HelloWorldProcess(WPSProcess):
    """
    Say hello to user ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="org.malleefowl.test.helloworld", 
            title="Hello World",
            version = "1.0",
            metadata = [],
            abstract="Welcome user and say hello ...",
            )

        self.user = self.addLiteralInput(
            identifier = "user",
            title = "Your name",
            abstract = "Please enter your name",
            type = type(''),
            )
        
        self.output = self.addLiteralOutput(
            identifier = "output",
            title = "Welcome message",
            type = type(''))
                                           
    def execute(self):
        self.show_status("Starting ...", 5)
        self.output.setValue("Hello %s and welcome to WPS :)" % (self.user.getValue()))
        self.show_status("Done", 95)
    
class UltimateQuestionProcess(WPSProcess):
    """
    The ultimate process to test the status and update capabilities of the server
    The processes shoul be requested as follows:
    ../wps.py?request=execute
    &service=wps
    &version=1.0.0
    &identifier=ultimatequestionprocess
    &status=true
    &storeExecuteResponse=true

    Done by Jorge de Jesus (jmdj@pml.ac.uk) as suggested by Kor de Jong
    
    """
    def __init__(self):
        # init process
        WPSProcess.__init__(
            self,
            identifier="org.malleefowl.test.ultimatequestionprocess", #the same as the file name
            title="Answer to Life, the Universe and Everything",
            version = "2.0",
            metadata = [],
            abstract="Numerical solution that is the answer to Life, Universe and Everything. The process is an improvement to Deep Tought computer (therefore version 2.0) since it no longer takes 7.5 milion years, but only a few seconds to give a response, with an update of status every 10 seconds.",
            )
            #No need for inputs since Execute will start the process
        self.Answer = self.addLiteralOutput(
            identifier = "answer",
            title = "The numerical answer to Life, Universe and Everything")
                                           
    def execute(self):
        import time
        self.show_status("Preparing....", 0)
        for i in xrange(1, 11):
            time.sleep(1)
            self.show_status("Thinking.....", i*10) 
        #The final answer    
        self.Answer.setValue("42")
        

class WordCountProcess(WPSProcess):
    """
    Counts words in a given text ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="org.malleefowl.test.wordcount", 
            title="Word Counter",
            version = "1.0",
            metadata = [],
            abstract="Counts words in a given text ...",
            )

        self.text = self.addComplexInput(
            identifier = "text",
            title = "Input text",
            abstract = "Input text",
            metadata=[],
            minOccurs=1,
            maxOccurs=1,
            formats=[{"mimeType":"text/plain"}],
            maxmegabites=2,
            upload=True,
            )
        
        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Word count result",
            metadata=[],
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        self.show_status("Starting ...", 5)

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

        self.show_status("Done", 95)

class ChomskyTextGeneratorProcess(WPSProcess):
    """
    Generates a random chomsky text ...
    http://code.activestate.com/recipes/440546-chomsky-random-text-generator/

    CHOMSKY is an aid to writing linguistic papers in the style
    of the great master.  It is based on selected phrases taken
    from actual books and articles written by Noam Chomsky.
    Upon request, it assembles the phrases in the elegant
    stylistic patterns that Chomsky is noted for.
    To generate n sentences of linguistic wisdom, type
        (CHOMSKY n)  -- for example
        (CHOMSKY 5) generates half a screen of linguistic truth.
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="org.malleefowl.test.chomsky", 
            title="Chomsky test generator",
            version = "1.0",
            metadata = [],
            abstract=" Generates a random chomsky text ...",
            )

        self.times = self.addLiteralInput(
            identifier="times",
            title="Times",
            abstract="Number of sentences to generate.",
            default="5",
            type=type(1),
            minOccurs=0,
            maxOccurs=1,
            )

        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Chomsky text",
            metadata=[],
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        self.show_status("Starting ...", 5)

        leadins = """To characterize a linguistic level L,
        On the other hand,
        This suggests that
        It appears that
        Furthermore,
        We will bring evidence in favor of the following thesis:
        To provide a constituent structure for T(Z,K),
        From C1, it follows that
        For any transformation which is sufficiently diversified in application to be of any interest,
        Analogously,
        Clearly,
        Note that
        Of course,
        Suppose, for instance, that
        Thus
        With this clarification,
        Conversely,
        We have already seen that
        By combining adjunctions and certain deformations,
        I suggested that these results would follow from the assumption that
        If the position of the trace in (99c) were only relatively inaccessible to movement,
        However, this assumption is not correct, since
        Comparing these examples with their parasitic gap counterparts in (96) and (97), we see that
        In the discussion of resumptive pronouns following (81),
        So far,
        Nevertheless,
        For one thing,
        Summarizing, then, we assume that
        A consequence of the approach just outlined is that
        Presumably,
        On our assumptions,
        It may be, then, that
        It must be emphasized, once again, that
        Let us continue to suppose that
        Notice, incidentally, that """
        # List of LEADINs to buy time.

        subjects = """ the notion of level of grammaticalness
        a case of semigrammaticalness of a different sort
        most of the methodological work in modern linguistics
        a subset of English sentences interesting on quite independent grounds
        the natural general principle that will subsume this case
        an important property of these three types of EC
        any associated supporting element
        the appearance of parasitic gaps in domains relatively inaccessible to ordinary extraction
        the speaker-hearer's linguistic intuition
        the descriptive power of the base component
        the earlier discussion of deviance
        this analysis of a formative as a pair of sets of features
        this selectionally introduced contextual feature
        a descriptively adequate grammar
        the fundamental error of regarding functional notions as categorial
        relational information
        the systematic use of complex symbols
        the theory of syntactic features developed earlier"""
        # List of SUBJECTs chosen for maximum professorial macho.

        verbs = """can be defined in such a way as to impose
        delimits
        suffices to account for
        cannot be arbitrary in
        is not subject to
        does not readily tolerate
        raises serious doubts about
        is not quite equivalent to
        does not affect the structure of
        may remedy and, at the same time, eliminate
        is not to be considered in determining
        is to be regarded as
        is unspecified with respect to
        is, apparently, determined by
        is necessary to impose an interpretation on
        appears to correlate rather closely with
        is rather different from"""
        #List of VERBs chosen for autorecursive obfuscation.

        objects = """ problems of phonemic and morphological analysis.
        a corpus of utterance tokens upon which conformity has been defined by the paired utterance test.
        the traditional practice of grammarians.
        the levels of acceptability from fairly high (e.g. (99a)) to virtual gibberish (e.g. (98d)).
        a stipulation to place the constructions into these various categories.
        a descriptive fact.
        a parasitic gap construction.
        the extended c-command discussed in connection with (34).
        the ultimate standard that determines the accuracy of any proposed grammar.
        the system of base rules exclusive of the lexicon.
        irrelevant intervening contexts in selectional rules.
        nondistinctness in the sense of distinctive feature theory.
        a general convention regarding the forms of the grammar.
        an abstract underlying order.
        an important distinction in language use.
        the requirement that branching is not tolerated within the dominance scope of a complex symbol.
        the strong generative capacity of the theory."""
        # List of OBJECTs selected for profound sententiousness.

        import textwrap, random
        from itertools import chain, islice, izip

        def chomsky(times=5, line_length=72):
            parts = []
            for part in (leadins, subjects, verbs, objects):
                phraselist = map(str.strip, part.splitlines())
                random.shuffle(phraselist)
                parts.append(phraselist)
            output = chain(*islice(izip(*parts), 0, times))
            return textwrap.fill(' '.join(output), line_length)

        outfile = self.mktempfile(suffix='.txt')
        with open(outfile, 'w') as fout:
            logger.debug('writing to %s', outfile)
            fout.write( chomsky(self.times.getValue()) )
            self.output.setValue( fout.name )

        self.show_status("Done", 95)


class InOutProcess(WPSProcess):
    """
    This process defines several types of literal type of in- and outputs.
    """

    def __init__(self):
        # definition of this process
        WPSProcess.__init__(
            self, 
            identifier = "org.malleefowl.test.inout",
            title="Testing all Data Types",
            version = "0.2",
            # TODO: what can i do with this?
            metadata=[
                {"title":"Foobar","href":"http://foo/bar"},
                {"title":"Barfoo","href":"http://bar/foo"},
                ],
            abstract="Just testing data types like date, datetime etc ...",
            )

        # Literal Input Data
        # ------------------

        # TODO: use also uom (unit=meter ...)
        self.intIn = self.addLiteralInput(
            identifier="int",
            title="Integer",
            abstract="This is an Integer",
            default="10",
            type=type(1),
            minOccurs=0,
            maxOccurs=1,
            )

        self.stringIn = self.addLiteralInput(
            identifier="string",
            title="String",
            abstract="This is a String",
            default="nothing important",
            type=type(''),
            minOccurs=0,
            maxOccurs=1,
            )

        self.floatIn = self.addLiteralInput(
            identifier="float",
            title="Float",
            abstract="This is a Float",
            default="3.14",
            type=type(0.1),
            minOccurs=0,
            maxOccurs=1,
            )

        self.booleanIn = self.addLiteralInput(
            identifier="boolean",
            title="Boolean",
            abstract="This is a Boolean",
            default=False,
            type=type(False),
            minOccurs=0,
            maxOccurs=1,
            )

        self.dateIn = self.addLiteralInput(
            identifier="date",
            title="Date",
            abstract="This is a Date: 2013-07-10",
            default="2013-07-11",
            type=type(date(2013,7,11)),
            minOccurs=0,
            maxOccurs=1,
            )

        self.stringChoiceIn = self.addLiteralInput(
            identifier="stringChoice",
            title="String Choice",
            abstract="Choose a string",
            default="one",
            type=type(''),
            minOccurs=0,
            maxOccurs=3,
            allowedValues=['one', 'two', 'three']
            )

        self.intRequiredIn = self.addLiteralInput(
            identifier="intRequired",
            title="Integer Required",
            abstract="This is an required Integer",
            #default="10",
            type=type(1),
            minOccurs=1, # required
            maxOccurs=1,
            )

        self.stringMoreThenOneIn = self.addLiteralInput(
            identifier="stringMoreThenOne",
            title="More then One",
            abstract="This is a more then one String (0-2)",
            #default="one",
            type=type(''),
            minOccurs=0,
            maxOccurs=2,
            )


        # complex input
        # -------------

        self.xml_upload = self.addComplexInput(
            identifier="xml_upload",
            title="XML Upload",
            abstract="Upoad XML File",
            metadata=[],
            minOccurs=0,
            maxOccurs=2,
            formats=[{"mimeType":"text/xml"}],
            maxmegabites=2,
            upload=True,
            )

        self.netcdf_upload = self.addComplexInput(
            identifier="netcdf_upload",
            title="NetCDF Upload",
            abstract="Upoad NetCDF File",
            metadata=[],
            minOccurs=0,
            maxOccurs=1,
            formats=[{"mimeType":"application/x-netcdf"}],
            maxmegabites=20,
            upload=True,
            )

        self.xml_url = self.addComplexInput(
            identifier="xml_url",
            title="XML File",
            abstract="URL of XML File",
            metadata=[],
            minOccurs=0,
            maxOccurs=2,
            formats=[{"mimeType":"text/xml"}],
            maxmegabites=2,
            )

        # zero or more bounding-boxes
        # --------------------------

        # TODO: bbox does not work yet in owslib

        # self.bboxIn = self.addBBoxInput(
        #     identifier="bbox",
        #     title="Bounding Box",
        #     abstract="Enter a bounding box",
        #     metadata=[], #TODO: what for?
        #     minOccurs=0,
        #     maxOccurs=2,
        #     crss=["EPSG:4326"],
        #     )

        self.dummyBBoxIn = self.addLiteralInput(
            identifier="dummybbox",
            title="Dummy BBox",
            abstract="This is a BBox: (minx,miny,maxx,maxy)",
            default="0,-90,180,90",
            type=type(''),
            minOccurs=1,
            maxOccurs=1,
            )

        # Output data
        # ===================================================

        # Literal output
        # --------------

        # TODO: use also uom (unit=meter ...)
        self.intOut = self.addLiteralOutput(
            identifier="int",
            title="Integer",
            abstract="This is an Integer",
            #metadata=[],
            #default=None,
            type=type(1),
            #uoms=(),
            #asReference=False,
            )

        self.stringOut = self.addLiteralOutput(
            identifier="string",
            title="String",
            abstract="This is a String",
            default=None,
            type=type(''),
            )

        self.floatOut = self.addLiteralOutput(
            identifier="float",
            title="Float",
            abstract="This is a Float",
            type=type(0.1),
            )

        self.booleanOut = self.addLiteralOutput(
            identifier="boolean",
            title="Boolean",
            abstract="This is a Boolean",
            type=type(False),
            )

        self.dateOut = self.addLiteralOutput(
            identifier="date",
            title="Date",
            abstract="This is a Date: 2013-07-10",
            type=type(date(2013,7,11)),
            )

        self.stringChoiceOut = self.addLiteralOutput(
            identifier="stringChoice",
            title="String Choice",
            abstract="Choosen string",
            default="one",
            type=type('')
            )

        self.intRequiredOut = self.addLiteralOutput(
            identifier="intRequired",
            title="Integer Required",
            abstract="This is an required Integer",
            type=type(1),
            )

        self.stringMoreThenOneOut = self.addLiteralOutput(
            identifier="stringMoreThenOne",
            title="More then One",
            abstract="This is a more then one String (0-2)",
            #default="one",
            type=type(''),
            )

        # complex output
        # -------------

        self.xmlFileOut = self.addComplexOutput(
            identifier="xmlfile",
            title="XML File",
            abstract="xml file",
            metadata=[],
            formats=[{"mimeType":"text/xml"}],
            asReference=True,
            )

        self.xml_upload_out = self.addComplexOutput(
            identifier="xml_upload",
            title="Uploaded XML File",
            abstract="Uploaded XML File",
            metadata=[],
            formats=[{"mimeType":"text/xml"}],
            asReference=True,
            )

        self.netcdf_upload_out = self.addComplexOutput(
            identifier="netcdf_upload",
            title="Uploaded NetCDF File",
            abstract="Uploaded NetCDF File",
            metadata=[],
            formats=[{"mimeType":"application/x-netcdf"}],
            asReference=True,
            )

        self.xml_url_out = self.addComplexOutput(
            identifier="xml_url",
            title="XML File",
            abstract="XML File given by URL",
            metadata=[],
            formats=[{"mimeType":"text/xml"}],
            asReference=True,
            )

        # bounding-box
        # --------------------------

        # self.bboxOut = self.addBBoxOutput(
        #     identifier="bbox",
        #     title="Bounding Box",
        #     abstract="Enter a bounding box",
        #     dimensions=2,
        #     crs="EPSG:4326",
        #     asReference=False
        #     )

        self.dummyBBoxOut = self.addLiteralOutput(
            identifier="dummybbox",
            title="Dummy BBox",
            abstract="This is a BBox: (minx,miny,maxx,maxy)",
            #default="0,-90,180,90",
            type=type(''),
            )
       
    def execute(self):
        self.show_status('execute inout', 10)

        print 'start testing all data types'

        # literals
        self.setOutputValue(
            identifier='intOut', 
            value=self.getInputValue(identifier='intIn'))

        self.stringOut.setValue(self.stringIn.getValue())
        self.floatOut.setValue(self.floatIn.getValue())
        self.booleanOut.setValue(self.booleanIn.getValue())
        self.dateOut.setValue(self.dateIn.getValue())
        self.intRequiredOut.setValue(self.intRequiredIn.getValue())
        self.stringChoiceOut.setValue(self.stringChoiceIn.getValue())

        # more than one
        # TODO: handle multiple values (fix in pywps)
        value = self.stringMoreThenOneIn.getValue()
        logger.debug('stringMoreThenOneIn = %s', value)
        if value != None:
            if type(value) == types.ListType:
                values = value
            else:
                values = [value]
            self.stringMoreThenOneOut.setValue( ','.join(values) )

        #TODO: bbox does not work yet
        #self.bboxOut.setValue(self.bboxIn.getValue())
        self.dummyBBoxOut.setValue(self.dummyBBoxIn.getValue())

        # complex
        # write my own
        logger.debug('write my own xml')
        xml_filename = self.mktempfile(suffix='.xml')
        with open(xml_filename, 'w') as fp:
            fp.write('<xml>just testing</xml>')
            fp.close()
            self.xmlFileOut.setValue( fp.name )

        # write uploaded file from input data
        logger.debug('write input xml1')
        xml_filename = self.mktempfile(suffix='.xml')
        with open(xml_filename, 'w') as fp:
            xml_upload = self.xml_upload.getValue()
            if xml_upload is not None:
                for xml in xml_upload:
                    logger.debug('read xml')
                    with open(xml, 'r') as fp2:
                        logger.debug('reading content')
                        fp.write( fp2.read() )
            else:
                fp.write( "<result>nothing</result>" )
            self.xml_upload_out.setValue( fp.name )

        # output uploaded netcdf file
        filename = self.netcdf_upload.getValue()
        if filename is not None:
            self.netcdf_upload_out.setValue( filename )
            
        # write file with url from input data
        logger.debug('write input xml_upload')
        xml_filename = self.mktempfile(suffix='.xml')
        with open(xml_filename, 'w') as fp:
            xml_url = self.xml_url.getValue()
            if xml_url is not None:
                for xml in xml_url:
                    logger.debug('read xml')
                    with open(xml, 'r') as fp2:
                        logger.debug('reading content')
                        fp.write( fp2.read() )
            else:
                fp.write( "<result>nothing</result>" )
            self.xml_url_out.setValue( fp.name )

        self.show_status("inout process ... done", 95)
        return
        
