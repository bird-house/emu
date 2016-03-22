from pywps.Process import WPSProcess

import logging
logger = logging.getLogger()

class BBoxProcess(WPSProcess):
    """
    This process has a boundingbox input and output parameter.
    """

    def __init__(self):
        WPSProcess.__init__(
            self, 
            identifier="bbox",
            title="Bounding Box",
            version="0.1",
            metadata=[
                {"title":"home","href":"http://emu.readthedocs.org/en/latest/index.html"},
                ],
            abstract="Testing BoundingBox Input/Output Parameter",
            statusSupported=True,
            storeSupported=True
            )

        self.bboxIn = self.addBBoxInput(
            identifier="bbox",
            title="Bounding Box",
            minOccurs=1,
            maxOccurs=1,
            crss=["EPSG:4326", "EPSG:3035"],
            )

        self.bboxOut = self.addBBoxOutput(
            identifier="bbox",
            title="Bounding Box",
            dimensions=2,
            crs="EPSG:4326",
            asReference=False,
            )

       
    def execute(self):
        # TODO: bbox output is not working as expected in pywps
        bbox = self.bboxIn.getValue()
        if bbox is not None:
            self.status.set("bbox={0}".format(bbox.coords), 90)
        self.bboxOut.setValue(bbox.coords)

        self.status.set("Done", 100)
        
