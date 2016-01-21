import tempfile
from pywps.Process import WPSProcess

class MultipleSource(WPSProcess):
    """
    Has multiple different sources
    """
    def __init__(self):
        WPSProcess.__init__(
            self,
            identifier="multiplesources", 
            title="Multiple Sources",
            version = "0.3",
            abstract="Process with multiple different sources ...",
            statusSupported=True,
            storeSupported=True
            )

        self.model_data = self.addComplexInput(
            identifier = "model",
            title = "Model data",
            abstract = "URL of NetCDF model data file",
            minOccurs=0,
            maxOccurs=100,
            formats=[{"mimeType":"application/netcdf"}],
            maxmegabites=100,
            )

        self.obs_data = self.addComplexInput(
            identifier = "obs",
            title = "Observational data",
            abstract = "URL of NetCDF observational data file",
            minOccurs=0,
            maxOccurs=100,
            formats=[{"mimeType":"application/netcdf"}],
            maxmegabites=100,
            )
        
        self.output = self.addComplexOutput(
            identifier = "output",
            title = "Model comparison result",
            formats=[{"mimeType":"text/plain"}],
            asReference=True,
            )
                                           
    def execute(self):
        model_files = self.getInputValues(identifier='model')
        obs_files = self.getInputValues(identifier='obs')

        _,outfile = tempfile.mkstemp(suffix='.txt')
        with open(outfile, 'w') as fout: 
            fout.write('Comparing {0} model files with {0} obs files\n\n'.format(len(model_files), len(obs_files)))
            self.output.setValue( fout.name )

        self.status.set("Done", 100)

