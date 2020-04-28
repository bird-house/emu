# -*- encoding: utf-8 -*-
from pywps import Service

from .common import client_for
from emu.processes import processes


def test_wps_caps():
    client = client_for(Service(processes=processes))
    resp = client.get(service='wps', request='getcapabilities', version='1.0.0', language='en-US')
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
        #'nc_to_dap',
        'ncmeta',
        'ncml',
        'non.py-id',
        'output_formats',
        'poly_centroid',
        'show_error',
        'simple_dry_run',
        'sleep',
        'translation',
        'ultimate_question',
        'wordcounter',
    ]

    # caps language
    assert resp.xpath('/wps:Capabilities/@xml:lang')[0] == "en-US"

    # supported languages
    languages = resp.xpath_text('/wps:Capabilities'
                                '/wps:Languages'
                                '/wps:Supported'
                                '/ows:Language')
    assert 'en-US' in languages
    assert 'fr-CA' in languages
    assert 'de-DE' in languages
