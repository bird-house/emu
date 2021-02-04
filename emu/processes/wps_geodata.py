"""
Process using an application/geo+json and 'image/tiff; application=geotiff' output. Used to test UI interactions.

Author: Trevor James Smith
"""
from pathlib import Path
from pywps import Process, ComplexOutput
from pywps import FORMATS
import logging


LOGGER = logging.getLogger("PYWPS")

__all__ = ["GeoData"]

DATA_DIR = Path(__file__).parent.parent.joinpath('data')


class GeoData(Process):
    def __init__(self):
        inputs = list()
        outputs = [
            ComplexOutput(
                "raster",
                "DEM subset of `shape` region in GeoTIFF format.",
                abstract="Elevation statistics: min, max, mean, median, sum, nodata",
                as_reference=True,
                supported_formats=[FORMATS.GEOTIFF],
            ),
            ComplexOutput(
                "vector",
                "Region definition in GeoJSON format",
                abstract="The original vector but buffered by a distance of 5.",
                as_reference=True,
                supported_formats=[FORMATS.GEOJSON, FORMATS.JSON],
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
        response.update_status("PyWPS Process started.", 0)

        geojson_out = response.outputs['vector']
        if geojson_out.data_format.mime_type == FORMATS.GEOJSON.mime_type:
            geojson_out.file = DATA_DIR.joinpath('Olympus_Mons.geojson')

        geotiff_out = response.outputs['raster']
        if geotiff_out.data_format.mime_type == FORMATS.GEOTIFF.mime_type:
            geotiff_out.file = DATA_DIR.joinpath('Olympus.tif')

        response.update_status("PyWPS Process completed.", 100)

        return response
