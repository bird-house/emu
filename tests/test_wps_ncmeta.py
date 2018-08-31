import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file
from emu.processes.wps_ncmeta import NCMeta

OPENDAP_URL = 'http://test.opendap.org:80/opendap/netcdf/examples/sresa1b_ncar_ccsm3_0_run1_200001.nc'
NC_URL = 'http://test.opendap.org:80/opendap/netcdf/examples/sresa1b_ncar_ccsm3_0_run1_200001.nc.nc4'
NC_FILE_URL = "file://{}".format(resource_file('test.nc'))


@pytest.mark.online
def test_wps_ncmeta_opendap():
    client = client_for(Service(processes=[NCMeta()]))
    datainputs = "dataset_opendap=@xlink:href={0}".format(OPENDAP_URL)
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
