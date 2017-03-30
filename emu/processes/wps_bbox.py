import os
import tempfile
from pywps.app.Common import Metadata

__author__ = 'Jachym'

from pywps import Process, BoundingBoxInput, BoundingBoxOutput

import logging
LOGGER = logging.getLogger('PYWPS')


class Box(Process):
    def __init__(self):
        inputs = [
            BoundingBoxInput('bbox', 'Bounding Box',
                             abstract='Bounding Box Input.',
                             crss=['epsg:4326', 'epsg:3035'],
                             min_occurs=0)
        ]
        outputs = [
            BoundingBoxOutput('bbox', 'Bounding Box',
                              abstract='Bounding Box Output.',
                              crss=['epsg:4326'])
        ]

        super(Box, self).__init__(
            self._handler,
            identifier='bbox',
            version='0.2',
            title="Bounding box in- and out",
            abstract='Give bounding box, return the same',
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/')],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.debug('bbox: coords=%s, crs=%s', request.inputs['bbox'][0].data, request.inputs['bbox'][0].crs)
        response.outputs['bbox'].data = request.inputs['bbox'][0].data
        response.outputs['bbox'].crs = request.inputs['bbox'][0].crs
        return response
