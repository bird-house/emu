from pywps import Service
from pywps.tests import assert_response_success
from emu.processes.wps_geodata import GeoData
from .common import client_for, CFG_FILE, get_output


class TestGeoData:
    def test_wps_geodata(self):

        client = client_for(Service(processes=[GeoData()], cfgfiles=CFG_FILE))

        resp = client.get(
            service='wps', request='execute', version='1.0.0',
            identifier='geodata', asobj=True)

        assert_response_success(resp)
        assert set(get_output(resp.xml).keys()) == {"vector", "raster"}
