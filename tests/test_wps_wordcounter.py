import nose.tools
from nose.plugins.attrib import attr

from tests.common import WpsTestClient, assert_response_success

@attr('online')
def test_wps_wordcount():
    wps = WpsTestClient()
    datainputs = "text={0}".format("https://en.wikipedia.org/wiki/Web_Processing_Service")
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='wordcount',
                   datainputs=datainputs)
    assert_response_success(resp)
