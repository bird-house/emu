import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file
from emu.processes.wps_ncmeta import NCMeta

OPENDAP_URL = 'http://www.esrl.noaa.gov/psd/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc'
NC_URL = 'https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis.derived/surface/air.mon.ltm.nc'
NC_FILE_URL = "file://{}".format(resource_file('test.nc'))


@pytest.mark.online
def test_wps_ncmeta_opendap():
    client = client_for(Service(processes=[NCMeta()]))
    datainputs = "dataset=@xlink:href={0}".format(OPENDAP_URL)
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='ncmeta',
        datainputs=datainputs)
    assert_response_success(resp)


@pytest.mark.online
def test_wps_ncmeta_netcdf():
    client = client_for(Service(processes=[NCMeta()]))
    datainputs = "dataset=@xlink:href={0}".format(NC_URL)
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='ncmeta',
        datainputs=datainputs)
    assert_response_success(resp)


def test_wps_ncmeta_file():
    client = client_for(Service(processes=[NCMeta()]))
    datainputs = "dataset=@xlink:href={0}".format(NC_FILE_URL)
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='ncmeta',
        datainputs=datainputs)
    assert_response_success(resp)
