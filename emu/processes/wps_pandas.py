import logging

from pywps import FORMATS, Format, ComplexInput, ComplexOutput, Process
from pywps.app.Common import Metadata

LOGGER = logging.getLogger("PYWPS")


class Pandas(Process):
    """
    Notes:

    Create some statisics with pandas from a CSV file.
    """
    def __init__(self):
        inputs = [
            ComplexInput('csv', 'CSV document',
                         abstract='A CSV document',
                         supported_formats=[Format('text/csv', extension='.csv'), FORMATS.TEXT]), ]
        outputs = [
            ComplexOutput('output', 'Output',
                          as_reference=True,
                          supported_formats=[FORMATS.JSON]), ]

        super(Pandas, self).__init__(
            self._handler,
            identifier='pandas',
            title='Pandas',
            abstract="Create statisics using Pandas",
            version='1.0',
            metadata=[
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/')
            ],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True)

    def _handler(self, request, response):
        # optional dependency
        import pandas as pd
        # start
        response.update_status('Pandas Process started.', 0)
        # read csv
        df = pd.read_csv(request.inputs['csv'][0].stream)
        # convert to json
        response.outputs['output'].data = df.to_json(orient='records')
        # done
        response.update_status('Pandas Process completed.', 100)
        return response
