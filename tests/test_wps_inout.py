import nose.tools
from nose.plugins.attrib import attr

from tests.common import WpsTestClient, assert_response_success

def test_wps_inout():
    wps = WpsTestClient()
    datainputs = "[intRequired=10]"
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='inout',
                   datainputs=datainputs)
    assert_response_success(resp)
