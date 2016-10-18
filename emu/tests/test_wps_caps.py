import pytest

from emu.tests.common import client_for


@pytest.mark.skip(reason="init pywps service")
def test_caps():
    client = client_for()
    resp = client.get(service='wps', request='getcapabilities')
    names = resp.xpath_text('/wps:Capabilities'
                            '/wps:ProcessOfferings'
                            '/wps:Process'
                            '/ows:Identifier')
    assert sorted(names.split()) == [
        'bbox', 'chomsky', 'dummyprocess',
        'hello', 'inout', 'ultimate_question', 'wordcount']
