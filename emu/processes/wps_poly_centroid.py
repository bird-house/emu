"""
Process using an application/xml+gml input. Used to test UI interactions.

Author: David Huard and Trevor James Smith
"""
from pywps import Process, ComplexInput, LiteralInput, LiteralOutput
from pywps import FORMATS
import logging
LOGGER = logging.getLogger("PYWPS")


class PolyCentroid(Process):
    def __init__(self):
        inputs = [
            LiteralInput("wkt", "Region definition in WKT: Well-Known-Text format",
                         abstract="A Well-Known-Test definition for a region.",
                         min_occurs=0, data_type="string", default=""),
            ComplexInput('xml', 'Region definition in XML format',
                         abstract="A polygon defining a region.",
                         min_occurs=0, supported_formats=[FORMATS.GML, ]),
        ]
        outputs = [
            LiteralOutput('output', 'The centroid of the polygon geometry.',
                          abstract="The coordinates of the polygon's approximate centroid.",)
        ]

        super(PolyCentroid, self).__init__(
            self._handler,
            identifier='poly_centroid',
            title="Approximate centroid of a polygon.",
            abstract="Return the polygon's centroid coordinates. If the geometry contains multiple polygons, "
                     "only the centroid of the first one will be computed. Do not use for serious computations"
                     ", this is only a test process and uses a crude approximation.",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    @staticmethod
    def _handler(request, response):
        from geomet import wkt
        from defusedxml import ElementTree
        response.update_status('PyWPS Process started.', 0)

        coordinates = None

        if request.inputs['wkt'][0].data != "":

            try:
                fn = request.inputs['wkt'][0].data
                poly = wkt.loads(fn)

                # Get the coordinates of the first feature
                if len(poly['coordinates']) == 1:  # For Polygons and Multipolygons
                    coordinates = poly['coordinates'][0]
                else:
                    coordinates = poly['coordinates']  # For other geometries

            except Exception as e:
                msg = "{}: WKT not found.".format(e)
                logging.warning(msg=msg)
                raise

        elif request.inputs['xml'][0].file is not None:

            try:
                fn = request.inputs['xml'][0].file
                poly = ElementTree.parse(fn)
                ns = {'gml': 'http://www.opengis.net/gml'}

                # Find the first polygon in the file.
                e = poly.find('.//gml:Polygon', ns)

                # Get the coordinates
                c = e.find('.//gml:coordinates', ns).text
                coordinates = [tuple(map(float, p.split(','))) for p in c.split(' ')]

            except Exception as e:
                msg = "{}: XML not found.".format(e)
                logging.warning(msg=msg)
                raise
        else:
            raise ValueError("Process requires a WKT string or XML file.")

        # Compute the average
        n = len(coordinates)
        x, y = zip(*coordinates)
        centroid_x = sum(x) / n
        centroid_y = sum(y) / n

        response.outputs['output'].data = '{:.5f},{:.5f}'.format(centroid_x, centroid_y)

        response.update_status('PyWPS Process completed.', 100)
        return response
