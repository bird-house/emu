from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, get_output
from emu.processes.wps_bbox import Box


def test_wps_bbox_1():
    client = client_for(Service(processes=[Box()]))
    datainputs = "bbox=20,42,24,46"

    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='bbox',
        datainputs=datainputs)
    # print(resp.data)
    assert_response_success(resp)
    assert '<ows:LowerCorner> 20.0  42.0 </ows:LowerCorner>' in str(resp.data)
    assert '<ows:UpperCorner> 24.0  46.0 </ows:UpperCorner>' in str(resp.data)


def test_wps_bbox_2():
    client = client_for(Service(processes=[Box()]))
    datainputs = "bbox=46,102,47,103,urn:ogc:def:crs:EPSG:6.6:4326,2"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='bbox',
        datainputs=datainputs)
    # print(resp.data)
    assert_response_success(resp)
    assert '<ows:LowerCorner> 46.0  102.0 </ows:LowerCorner>' in str(resp.data)
    assert '<ows:UpperCorner> 47.0  103.0 </ows:UpperCorner>' in str(resp.data)
