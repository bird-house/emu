import os
import tempfile
from pywps.app.Common import Metadata

__author__ = 'Jachym'

from pywps import Process, BoundingBoxInput, BoundingBoxOutput


class Box(Process):
    def __init__(self):
        inputs = [
            # BoundingBoxInput('bboxin', 'box in',
            #                 crss=['epsg:4326', 'epsg:3035'],
            #                 min_occurs=0)
        ]
        outputs = [
            BoundingBoxOutput('bboxout', 'box out',
                              abstract='Bounding Box Output',
                              crss=['epsg:4326'])
        ]

        super(Box, self).__init__(
            self._handler,
            identifier='bbox',
            version='0.1',
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
        response.outputs['bboxout'].data = [0, 0, 10, 10]
        return response
