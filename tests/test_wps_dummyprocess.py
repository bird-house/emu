from tests.common import WpsTestClient, assert_response_success

def test_wps_dummyprocess():
    wps = WpsTestClient()
    datainputs = "[input1=10;input2=2]"
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='dummyprocess',
                   datainputs=datainputs)
    assert_response_success(resp)
