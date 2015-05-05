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
            identifier="helloworld", 
            title="Hello World",
            version = "1.0",
            metadata = [{"title":"Documentation","href":"http://emu.readthedocs.org/en/latest/"}],
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
        self.show_status("Starting ...", 1)
        self.output.setValue("Hello %s and welcome to WPS :)" % (self.user.getValue()))
        self.show_status("Done", 100)
