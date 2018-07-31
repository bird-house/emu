import os
import requests
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file, TESTS_HOME, WPS, OWS, get_output
from emu.processes.wps_poly_centroid import PolyCentroid

cfgfiles = os.path.join(TESTS_HOME, 'test.cfg')


def test_wps_poly_centroid_get():
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    datainputs = "polygon=@xlink:href=file://{0}".format(resource_file('poly.xml'))
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='poly_centroid',
        datainputs=datainputs)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "119.59740,-13.57388"}


def test_wps_poly_centroid_post():
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    request_doc = WPS.Execute(
        OWS.Identifier('poly_centroid'),
        WPS.DataInputs(
            WPS.Input(
                OWS.Identifier('polygon'),
                WPS.Data(WPS.ComplexData(open(resource_file('poly.xml'), 'r').read()))
            )
        ),
        version='1.0.0'
    )
    resp = client.post_xml(doc=request_doc)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output': "119.59740,-13.57388"}
