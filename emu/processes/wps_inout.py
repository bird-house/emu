from datetime import datetime, date
import types
import tempfile

from pywps.Process import WPSProcess

class InOutProcess(WPSProcess):
    """
    This process defines several types of literal type of in- and outputs.

    TODO: add literal input with value range[(0,100)] ... see pywps doc
    """

    def __init__(self):
        # definition of this process
        WPSProcess.__init__(
            self, 
            identifier="inout",
            title="Testing all Data Types",
            version="0.4",
            # TODO: what can i do with this?
            metadata=[
                {"title":"Foobar","href":"http://foo/bar"},
                {"title":"Barfoo","href":"http://bar/foo"},
                ],
            abstract="Just testing data types like date, datetime etc ...",
            statusSupported=True,
            storeSupported=True
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
        _,xml_filename = tempfile.mkstemp(suffix='.xml')
        with open(xml_filename, 'w') as fp:
            fp.write('<xml>just testing</xml>')
            fp.close()
            self.xmlFileOut.setValue( fp.name )

        # write file with url from input data
        _,xml_filename = tempfile.mkstemp(suffix='.xml')
        with open(xml_filename, 'w') as fp:
            xml_url = self.xml_url.getValue()
            if xml_url is not None:
                for xml in xml_url:
                    with open(xml, 'r') as fp2:
                        fp.write( fp2.read() )
            else:
                fp.write( "<result>nothing</result>" )
            self.xml_url_out.setValue( fp.name )

        self.status.set("Done", 100)
        
