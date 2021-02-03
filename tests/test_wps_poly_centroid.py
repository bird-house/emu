import os
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file, TESTS_HOME, WPS, OWS, get_output
from emu.processes.wps_poly_centroid import PolyCentroid

cfgfiles = os.path.join(TESTS_HOME, 'test.cfg')


def test_wps_xml_centroid_get():
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    datainputs = f"xml=@xlink:href=file://{resource_file('poly.xml')}"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='poly_centroid',
        datainputs=datainputs)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "119.59740,-13.57388"}


def test_wps_xml_centroid_post():
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    request_doc = WPS.Execute(
        OWS.Identifier('poly_centroid'),
        WPS.DataInputs(
            WPS.Input(
                OWS.Identifier('xml'),
                WPS.Data(WPS.ComplexData(open(resource_file('poly.xml'), 'r').read()))
            )
        ),
        version='1.0.0'
    )
    resp = client.post_xml(doc=request_doc)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "119.59740,-13.57388"}


def test_wps_wkt_centroid_get():
    wkt = "POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))"
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    datainputs = f"wkt={wkt}"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='poly_centroid',
        datainputs=datainputs)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "26.00000,24.00000"}


def test_wps_wkt_centroid_post():
    wkt = "POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))"
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    request_doc = WPS.Execute(
        OWS.Identifier('poly_centroid'),
        WPS.DataInputs(
            WPS.Input(
                OWS.Identifier('wkt'),
                WPS.Data(WPS.LiteralData(wkt))
            )
        ),
        version='1.0.0'
    )
    resp = client.post_xml(doc=request_doc)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "26.00000,24.00000"}
