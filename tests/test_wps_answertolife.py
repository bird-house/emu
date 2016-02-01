import nose.tools
from nose.plugins.attrib import attr

from tests.common import WpsTestClient, assert_response_success

@attr('slow')
def test_wps_ultimatequestionprocess():
    wps = WpsTestClient()
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='ultimatequestionprocess')
    assert_response_success(resp)
