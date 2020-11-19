from pywps.app.Common import Metadata
from pywps.ext_autodoc import MetadataUrl

__author__ = 'Jachym'

from pywps import Process, BoundingBoxInput, BoundingBoxOutput

import logging
LOGGER = logging.getLogger('PYWPS')


class Box(Process):
    def __init__(self):
        inputs = [
            BoundingBoxInput('bbox', 'Bounding Box',
                             abstract='Bounding Box Input.',
                             crss=['-12.0, 49.0, 3.0, 61.0,epsg:4326x', 'epsg:4326', 'epsg:3035'],
                             min_occurs=0,
                             max_occurs=1)
        ]
        outputs = [
            BoundingBoxOutput('bbox', 'Bounding Box',
                              abstract='Bounding Box Output.',
                              crss=['epsg:4326'])
        ]

        super(Box, self).__init__(
            self._handler,
            identifier='bbox',
            version='0.3',
            title="Bounding box in- and out",
            abstract='Give bounding box, return the same',
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                MetadataUrl('User Guide',
                            'http://emu.readthedocs.io/en/latest/',
                            anonymous=True)],
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        LOGGER.debug('bbox: coords=%s, crs=%s', request.inputs['bbox'][0].data, request.inputs['bbox'][0].crs)
        response.outputs['bbox'].data = request.inputs['bbox'][0].data
        response.outputs['bbox'].crs = request.inputs['bbox'][0].crs

        response.update_status('PyWPS Process completed.', 100)
        return response
