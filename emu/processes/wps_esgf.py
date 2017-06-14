from pywps import Process, LiteralInput, LiteralOutput, UOM
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")


class ESGFDemo(Process):
    def __init__(self):
        inputs = [
            LiteralInput('variable', 'Variable',
                         abstract='Choose a variable.',
                         metadata=[
                             Metadata('variable',
                                      role='https://www.earthsystemcog.org/spec/esgf_search/2.1.0/def/facet/variable',
                                      href='http://esgf-data.dkrz.de/esg-search/search?project=CMIP5&time_frequency=mon&distrib=false&replica=false&latest=true&limit=0&facets=variable'),  # noqa
                         ],
                         data_type='string',
                         allowed_values=['tas', 'tasmax', 'tasmin'],
                         default='tas')]
        outputs = [
            LiteralOutput('output', 'Output response',
                          abstract='A summary report.',
                          data_type='string')]

        super(ESGFDemo, self).__init__(
            self._handler,
            identifier='esgf_demo',
            title='ESGF Demo',
            abstract='Shows how to use WPS metadata for processes using ESGF data.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
                Metadata('Allowed CMIP5 Datasets',
                         role='https://www.earthsystemcog.org/spec/esgf_search/2.1.0/def/query',  # noqa
                         href='http://esgf-data.dkrz.de/esg-search/search?project=CMIP5&time_frequency=mon&variable=tas&distrib=false&replica=false&latest=true&limit=0&facets=model,experiment,ensemble,variable'),  # noqa
            ],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("starting ...")
        response.outputs['output'].data = 'Variable={0}'.format(request.inputs['variable'][0].data)
        response.update_status('done', 100)
        return response
