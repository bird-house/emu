import nose.tools
from nose.plugins.attrib import attr

from tests.common import WpsTestClient, assert_response_success

def test_wps_chomsky():
    wps = WpsTestClient()
    datainputs = "[times=10]"
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='chomsky',
                   datainputs=datainputs)
    assert_response_success(resp)
