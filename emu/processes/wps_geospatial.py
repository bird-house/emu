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
                min_occurs=0,
                max_occurs=1,
                supported_formats=[FORMATS.GEOTIFF],
            ),
            ComplexInput(
                "vector",
                "Region definition in GeoJSON format",
                abstract="A polygon defining a region.",
                min_occurs=0,
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

    @staticmethod
    def _handler(self, request, response):
        import tempfile

        from shapely.geometry import box, MultiPolygon
        import fiona
        import rasterio as rio
        from rasterio.mask import mask

        response.update_status("PyWPS Process started.", 0)

        if (
            request.inputs["vector"][0].file is None
            and request.inputs["raster"][0].file is None
        ):
            raise Exception("You need to provide at least one dataset.")

        rasters = list()
        for dataset in request.inputs["raster"]:
            rasters.append(dataset.file)

        centroid = 0, 0
        polygon = ""
        if request.inputs["vector"][0].file is not None:
            try:
                file = request.inputs["vector"][0].file
                vector = fiona.open(file)

                polygon = next(iter(vector))["geometry"]
                p = polygon["coordinates"][0]
                poly = MultiPolygon(p)
                centroid = poly.centroid.xy[:]

            except Exception as e:
                msg = "{}: unable to read vector file.".format(e)
                logging.warning(msg=msg)
                raise

        bounds = None
        subset_gtiff = None
        if rasters:
            bounds = list()
            for file in rasters:
                data = rio.open(file, mode="r")
                bounds.append(data.bounds)

                if not polygon:
                    # Clip the raster to a quadrant
                    w, s, e, n = data.bounds
                    x_0, y_0 = (e + w) / 2, (n + s) / 2
                    b = box(w, s, x_0, y_0)
                    m, _ = mask(dataset=data, shapes=[b], crop=True)
                else:
                    m, _ = mask(dataset=data, shapes=[polygon], crop=True)

                output_meta = data.meta.copy()
                output_meta.update(
                    dict(driver="GTiff", height=m.shape[1], width=m.shape[2])
                )
                subset_gtiff = tempfile.NamedTemporaryFile(
                    prefix="out_", suffix=".tiff", delete=False, dir=self.workdir
                ).name

                # Write to GeoTIFF
                with rio.open(subset_gtiff, "w", **output_meta) as f:
                    f.write(m, 1)

        response.outputs["centroid"].data = "{:.5f},{:.5f}".format(*centroid)
        response.outputs["bounds"].data = bounds
        response.outputs["raster"].file = subset_gtiff

        response.update_status("PyWPS Process completed.", 100)
        return response
