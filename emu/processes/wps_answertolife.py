from pywps.Process import WPSProcess

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
            identifier="ultimatequestionprocess", #the same as the file name
            title="Answer to Life, the Universe and Everything",
            version="2.1",
            abstract="Numerical solution that is the answer to Life, Universe and Everything. The process is an improvement to Deep Tought computer (therefore version 2.0) since it no longer takes 7.5 milion years, but only a few seconds to give a response, with an update of status every 10 seconds.",
            statusSupported=True,
            storeSupported=True
            )

        self.delay = self.addLiteralInput(
            identifier="delay",
            title="Delay",
            abstract="Delay in Seconds. Default: 1 second.",
            default=1,
            type=(1),
            )
        
        self.answer = self.addLiteralOutput(
            identifier = "answer",
            title = "The numerical answer to Life, Universe and Everything")
                                           
    def execute(self):
        import time
        self.status.set("Preparing....", 0)
        for i in xrange(1, 11):
            time.sleep( float(self.delay.getValue()) )
            self.status.set("Thinking.....", i*10) 
        #The final answer    
        self.answer.setValue("42")
        
