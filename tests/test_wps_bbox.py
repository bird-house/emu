import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_bbox import Box


# @pytest.mark.skip(reason="no way of currently testing this")
def test_wps_bbox():
    client = client_for(Service(processes=[Box()]))
    # datainputs = "bbox=101,42,110,46"
    datainputs = "bbox=46,102,47,103,urn:ogc:def:crs:EPSG:6.6:4326,2"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='bbox',
        datainputs=datainputs)
    # print(resp.data)
    assert_response_success(resp)
