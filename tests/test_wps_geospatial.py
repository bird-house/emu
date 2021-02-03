from pywps import Service
from pywps.tests import assert_response_success
from emu.processes.wps_geospatial import GeoData
from .common import client_for, CFG_FILE, resource_file


def test_wps_geodata():

    client = client_for(Service(processes=[GeoData()], cfgfiles=CFG_FILE))

    datainputs = f"vector=@xlink:href=file://{resource_file('Olympus_Mons.json')};" \
                 f"raster=@xlink:href=file://{resource_file('Olympus.tif')}"

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='geodata', datainputs=datainputs)

    assert_response_success(resp)


def test_wps_geodata_novector():

    client = client_for(Service(processes=[GeoData()], cfgfiles=CFG_FILE))

    datainputs = f"raster=@xlink:href=file://{resource_file('Olympus.tif')}"

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='geodata', datainputs=datainputs)

    assert_response_success(resp)


def test_wps_geodata_noraster():

    client = client_for(Service(processes=[GeoData()], cfgfiles=CFG_FILE))

    datainputs = f"vector=@xlink:href=file://{resource_file('Olympus_Mons.json')};"

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='geodata', datainputs=datainputs)

    assert_response_success(resp)
