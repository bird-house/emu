"""
Process using an application/geo+json and 'image/tiff; application=geotiff' input. Used to test UI interactions.

Author: Trevor James Smith
"""
from pywps import Process, ComplexInput, LiteralOutput, BoundingBoxOutput, ComplexOutput
from pywps import FORMATS
import logging

LOGGER = logging.getLogger("PYWPS")

__all__ = ["GeoData"]


class GeoData(Process):
    def __init__(self):
        inputs = [
            ComplexInput(
                "raster",
                "Raster grid of a general region.",
                abstract="A Well-Known-Test definition for a region.",
                min_occurs=1,
                max_occurs=1,
                supported_formats=[FORMATS.GEOTIFF],
            ),
            ComplexInput(
                "vector",
                "Region definition in GeoJSON format",
                abstract="A polygon defining a region.",
                min_occurs=1,
                max_occurs=1,
                supported_formats=[
                    FORMATS.GEOJSON,
                ],
            ),
        ]
        outputs = [
            LiteralOutput(
                "centroid",
                "The centroid of the polygon geometry.",
                abstract="The coordinates of the polygon's approximate centroid.",
            ),
            BoundingBoxOutput(
                "bounds",
                "The geographic boundary of a raster image.",
                abstract="The bounding box coordinates of a raster image (W/S/E/N).",
                crss=["epsg:4326"],
            ),
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
                supported_formats=[FORMATS.GEOJSON]
            )
        ]

        super(GeoData, self).__init__(
            self._handler,
            identifier="geodata",
            title="Centroid and bounding box for vector and raster data",
            abstract="Return the polygon's centroid coordinates. If the geometry contains multiple polygons, "
            "only the centroid of the first one will be computed. Do not use for serious computations"
            ", this is only a test process and uses a crude approximation.",
            version="1.0",
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True,
        )

    def _handler(self, request, response):
        import json
        import tempfile

        from shapely.geometry import mapping, shape
        import fiona
        import rasterio as rio
        from rasterio.mask import mask

        response.update_status("PyWPS Process started.", 0)

        vec_file = request.inputs["vector"][0].file
        ras_file = request.inputs["raster"][0].file

        response.update_status("Reading Vector file", 10)
        try:
            with fiona.open(vec_file, mode='r') as f:
                feature = next(iter(f))
                polygon = shape(feature["geometry"])
                bounds = [*polygon.bounds]
                centroid = polygon.centroid

                buffered = polygon.buffer(5)
                buffered_geojson = tempfile.NamedTemporaryFile(
                    prefix="out_", suffix=".geojson", delete=False, dir=self.workdir
                ).name
                response.update_status("Writing Vector file", 10)
                with open(buffered_geojson, "w") as bf:
                    output = {"type": "FeatureCollection", "features": []}
                    feature["geometry"] = mapping(buffered)
                    output["features"].append(feature)
                    bf.write(f"{json.dumps(output)}")

        except Exception as e:
            msg = f"{e}: unable to read vector file."
            logging.warning(msg=msg)
            raise

        response.update_status("Reading Raster file", 30)
        with rio.open(ras_file, mode="r") as data:
            # Clip the raster with the found shape
            masked, _ = mask(dataset=data, shapes=[polygon], crop=True)
            output_meta = data.meta.copy()
            output_meta.update(
                dict(driver="GTiff", height=masked.shape[1], width=masked.shape[2])
            )
            subset_geotiff = tempfile.NamedTemporaryFile(
                prefix="out_", suffix=".tiff", delete=False, dir=self.workdir
            ).name

            # Write to GeoTIFF
            response.update_status("Writing masked raster file", 70)
            with rio.open(subset_geotiff, "w", **output_meta) as f:
                f.write(masked)

        response.outputs["centroid"].data = "{:.5f},{:.5f}".format(
            centroid.x, centroid.y
        )
        response.outputs["bounds"].data = bounds
        response.outputs["raster"].file = subset_geotiff
        response.outputs["vector"].file = buffered_geojson

        response.update_status("PyWPS Process completed.", 100)

        return response
