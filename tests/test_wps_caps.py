from pywps import Service

from .common import client_for
from emu.processes import processes


def test_wps_caps():
    client = client_for(Service(processes=processes))
    resp = client.get(service='wps', request='getcapabilities', version='1.0.0')
    names = resp.xpath_text('/wps:Capabilities'
                            '/wps:ProcessOfferings'
                            '/wps:Process'
                            '/ows:Identifier')
    assert sorted(names.split()) == [
        'bbox',
        'binaryoperatorfornumbers',
        'chomsky',
        'dummyprocess',
        'esgf_demo',
        'hello',
        'inout',
        'multiple_outputs',
        'nap',
        'ncmeta',
        'ncml',
        'non.py-id',
        'output_formats',
        'poly_centroid',
        'show_error',
        'sleep',
        'ultimate_question',
        'wordcounter',
    ]
