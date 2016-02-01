import nose.tools
from tests.common import WpsTestClient

def test_caps():
    wps = WpsTestClient()
    resp = wps.get(service='wps', request='getcapabilities')
    names = resp.xpath_text('/wps:Capabilities'
                            '/wps:ProcessOfferings'
                            '/wps:Process'
                            '/ows:Identifier')
    assert sorted(names.split()) == ['chomsky', 'dummyprocess', 'helloworld', 'inout', 'multiplesources', 'ultimatequestionprocess', 'wordcount', 'zonal_mean']

