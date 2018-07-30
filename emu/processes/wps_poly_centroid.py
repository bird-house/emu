"""
Process using an application/xml+gml input. Used to test UI interactions.

Author: David Huard
"""
from pywps import Process, ComplexInput, LiteralOutput
from pywps import FORMATS
import logging
LOGGER = logging.getLogger("PYWPS")


class PolyCentroid(Process):
    def __init__(self):
        inputs = [
            ComplexInput('polygon', 'Region definition',
                         abstract="A polygon defining a region.",
                         supported_formats=[FORMATS.GML, ]),
        ]
        outputs = [
            LiteralOutput('centroid', 'The centroid of the polygon geometry.',
                          abstract="The coordinates of the polygon's approximate centroid.",)
        ]

        super(PolyCentroid, self).__init__(
            self._handler,
            identifier='poly_centroid',
            title="Approximate centroid of a polygon.",
            abstract="Return the polygon's centroid coordinates. If the geometry contains multiple polygons, "
                     "only the centroid of the first one will be computed. Do not use for serious computations"
                     ", this is only a test process and uses a crude approximation. ",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        from defusedxml import ElementTree
        fn = request.inputs['polygon'][0].file

        ns = {'gml': 'http://www.opengis.net/gml'}
        poly = ElementTree.parse(fn)

        # Find the first polygon in the file.
        e = poly.find('.//gml:Polygon', ns)

        # Get the coordinates
        c = e.find('.//gml:coordinates', ns).text
        coords = [tuple(map(float, p.split(','))) for p in c.split(' ')]

        # Compute the average
        n = len(coords)
        x, y = zip(*coords)
        cx = sum(x) / n
        cy = sum(y) / n

        response.outputs['centroid'].data = '{},{}'.format(cx, cy)
        return response
