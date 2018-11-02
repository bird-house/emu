from pywps import Process
from pywps import LiteralInput, LiteralOutput
from pywps import ComplexInput
from pywps import Format
from pywps.app.Common import Metadata

import logging
LOGGER = logging.getLogger("PYWPS")


class ESGFDemo(Process):
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'Dataset',
                         abstract='You may provide a URL or upload a NetCDF file.',
                         min_occurs=0,
                         max_occurs=100,
                         supported_formats=[Format('application/x-netcdf')]),
            LiteralInput('dataset_opendap', 'Remote OpenDAP Data URL',
                         data_type='string',
                         abstract="Or provide a remote OpenDAP data URL,"
                                  " for example:"
                                  " http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis2.dailyavgs/surface/mslp.2016.nc",  # noqa
                         metadata=[
                            Metadata(
                                'application/x-ogc-dods',
                                'https://www.iana.org/assignments/media-types/media-types.xhtml')],
                         min_occurs=0,
                         max_occurs=100)]
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
                Metadata('ESGF Constraints',
                         role='https://www.earthsystemcog.org/spec/esgf_search/4.12.0/def/constraints',  # noqa
                         href='http://esgf-data.dkrz.de/esg-search/search?project=CMIP5&time_frequency=mon&variable=tas,tasmax,tasmin&experiment=historical'),  # noqa
            ],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.info("starting ...")
        datasets = []
        # append file urls
        if 'dataset' in request.inputs:
            for dataset in request.inputs['dataset']:
                datasets.append(dataset.file)
        # append opendap urls
        if 'dataset_opendap' in request.inputs:
            for dataset in request.inputs['dataset_opendap']:
                datasets.append(dataset.data)
        if not datasets:
            raise Exception("You need to provide at least one dataset.")
        response.outputs['output'].data = 'Number of datasets = {}'.format(len(datasets))

        response.update_status('PyWPS Process completed.', 100)
        return response
