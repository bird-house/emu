import pytest

from pywps import Service
from pywps.tests import assert_response_success
from emu.processes.wps_geodata import GeoData
from emu.processes.wps_geospatial import GeoSpatial
from .common import client_for, CFG_FILE, resource_file


def test_wps_geospatial():

    client = client_for(Service(processes=[GeoSpatial()], cfgfiles=CFG_FILE))
    datainputs = f"vector=@xlink:href=file://{resource_file('Olympus_Mons.geojson')};" \
                 f"raster=@xlink:href=file://{resource_file('Olympus.tif')}"

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='geospatial', datainputs=datainputs)
    assert_response_success(resp)


def test_wps_geospatial_novector_fails():

    client = client_for(Service(processes=[GeoSpatial()], cfgfiles=CFG_FILE))
    datainputs = f"raster=@xlink:href=file://{resource_file('Olympus.tif')}"

    with pytest.raises(AssertionError):
        resp = client.get(
            service='wps', request='execute', version='1.0.0',
            identifier='geospatial', datainputs=datainputs)
        assert_response_success(resp)


def test_wps_geodata():

    client = client_for(Service(processes=[GeoData()], cfgfiles=CFG_FILE))

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='geodata')
    assert_response_success(resp)
