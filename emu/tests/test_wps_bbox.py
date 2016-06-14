from emu.tests.common import WpsTestClient, assert_response_success

def test_wps_bbox():
    wps = WpsTestClient()
    datainputs = "[bbox=101,42,110,46]"
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='bbox',
                   datainputs=datainputs)
    assert_response_success(resp)
