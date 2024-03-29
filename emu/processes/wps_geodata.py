"""
Process using an application/geo+json and 'image/tiff; application=geotiff' output. Used to test UI interactions.

Author: Trevor James Smith
"""
from pathlib import Path
from pywps import Process, ComplexOutput, ComplexInput
from pywps import FORMATS
from pywps.validator.mode import MODE
import logging


LOGGER = logging.getLogger("PYWPS")

__all__ = ["GeoData"]

DATA_DIR = Path(__file__).parent.parent.joinpath('data')


class GeoData(Process):
    def __init__(self):
        inputs = [ComplexInput("shape",
                               "Geometry",
                               supported_formats=[FORMATS.GEOJSON],
                               mode=MODE.NONE,  # Can be upgraded to STRICT once pywps releases 4.4.3 or 4.5.
                               min_occurs=0,
                               max_occurs=1)
                  ]
        outputs = [
            ComplexOutput(
                "raster",
                "DEM of region in GeoTIFF format.",
                abstract="Elevation data for Olympus Martian region in byte range.",
                as_reference=True,
                supported_formats=[FORMATS.GEOTIFF],
            ),
            ComplexOutput(
                "vector",
                "Region definition in GeoJSON format",
                abstract="Rough vector polygon of the Olympus Mons plateau.",
                as_reference=True,
                supported_formats=[FORMATS.GEOJSON],
            ),
        ]

        super(GeoData, self).__init__(
            self._handler,
            identifier="geodata",
            title="deliver vector and raster data",
            abstract="Return an example raster and vector dataset",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
        )

    @staticmethod
    def _handler(request, response):
        import json
        response.update_status("PyWPS Process started.", 0)

        if "shape" in request.inputs:
            LOGGER.info("Loading `shape`")
            json.loads(request.inputs["shape"][0].data)

        response.outputs['vector'].file = DATA_DIR / "Olympus_Mons.geojson"

        response.outputs['raster'].file = DATA_DIR / "Olympus.tif"

        response.update_status("PyWPS Process completed.", 100)

        return response
