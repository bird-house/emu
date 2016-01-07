from pywps.Process import WPSProcess
from malleefowl.process import show_status

class HelloWorldProcess(WPSProcess):
    """
    Say hello to user ...
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="helloworld", 
            title="Hello World",
            version = "1.1",
            metadata = [{"title":"Documentation","href":"http://emu.readthedocs.org/en/latest/"}],
            abstract="Welcome user and say hello ...",
            statusSupported=True,
            storeSupported=True
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
        show_status(self, "Starting ...", 0)
        self.output.setValue("Hello %s and welcome to WPS :)" % (self.user.getValue()))
        show_status(self, "Done", 100)
