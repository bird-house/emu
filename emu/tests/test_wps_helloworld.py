from emu.tests.common import WpsTestClient, assert_response_success

def test_wps_helloworld():
    wps = WpsTestClient()
    datainputs = "[user=LovelySugarBird]"
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='helloworld',
                   datainputs=datainputs)
    assert_response_success(resp)
