import json

from pywps import Service
from pywps import get_ElementMakerForVersion

from .common import client_for
from emu.processes.wps_show_defaults import ShowDefaults

VERSION = "1.0.0"

WPS, OWS = get_ElementMakerForVersion(VERSION)


def test_wps_show_defaults_post():
    client = client_for(Service(processes=[ShowDefaults()]))
    request_doc = WPS.Execute(
        OWS.Identifier('show_defaults'),
        WPS.DataInputs(
            WPS.Input(
                OWS.Identifier('string_0'),
                WPS.Data(WPS.LiteralData("ZERO"))
            ),
            # WPS.Input(
            #     OWS.Identifier('string_1'),
            #     WPS.Data(WPS.LiteralData("ONE"))
            # ),
            # WPS.Input(
            #     OWS.Identifier('string_2'),
            #     WPS.Data(WPS.LiteralData("TWO"))
            # ),
            WPS.Input(
                OWS.Identifier('string_3'),
                WPS.Data(WPS.LiteralData("THREE"))
            )
        ),
        WPS.ResponseForm(
            WPS.RawDataOutput(
                OWS.Identifier('output')
            )
        ),
        version='1.0.0'
    )
    resp = client.post_xml(doc=request_doc)
    print(resp.data)
    assert resp.status_code == 200
    result = json.loads(resp.data)
    assert result['string0'] == 'ZERO'
    assert result['string1'] == 'one'
    assert result['string2'] == 'two'
    assert result['string3'] == 'THREE'
