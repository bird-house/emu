from pywps import Process, LiteralInput, LiteralOutput
from pywps.inout.literaltypes import AllowedValue
from pywps.app.Common import Metadata
from pywps.app.exceptions import StorageLimitExceeded, DryRunWarning
from pywps.validator.mode import MODE

import logging
LOGGER = logging.getLogger("PYWPS")


class SimpleDryRun(Process):
    """An example of implementing a dry-run to protect your process from unwanted resource usage."""
    def __init__(self):
        inputs = [
            LiteralInput('dry_run', 'Dry run mode. Default false',
                         data_type='boolean',
                         default=False,),
            LiteralInput('count', 'Number of Files (Limit 10)',
                         abstract='How many files do you want to download? The limit is 10',
                         data_type='integer',
                         allowed_values=[AllowedValue(minval=1, maxval=20)],
                         default=1,
                         mode=MODE.SIMPLE), ]
        outputs = [
            LiteralOutput('output', 'Output response',
                          data_type='string')]

        super(SimpleDryRun, self).__init__(
            self._handler,
            identifier='simple_dry_run',
            title='Simple Dry Run',
            abstract='A dummy download as simple dry-run example.',
            metadata=[
                Metadata('User Guide', 'https://emu.readthedocs.io/en/latest/processes.html'),  # noqa
            ],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        # TODO: we need a more informational user exception in pywps.
        response.update_status('PyWPS Process started.', 0)

        num_files = request.inputs['count'][0].data

        if num_files > 10:
            msg = "Too many files too download"
            raise StorageLimitExceeded(msg, used=num_files, available=10)

        if request.inputs['dry_run'][0].data is True:
            raise DryRunWarning(storage_used="{} files".format(num_files), time_used="unknown")

        response.outputs['output'].data = 'File downloads done: {}'.format(num_files)
        response.update_status('PyWPS Process completed.', 100)
        return response
