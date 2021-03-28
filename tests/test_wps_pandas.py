import pytest
import json
from pywps import Service
from pywps.tests import assert_response_success
from pywps import get_ElementMakerForVersion

from .common import client_for, resource_file, get_output
from emu.processes.wps_pandas import Pandas

VERSION = "1.0.0"

WPS, OWS = get_ElementMakerForVersion(VERSION)


def test_wps_pandas_embedded():
    client = client_for(Service(processes=[Pandas()]))
    text = open(resource_file("penguins.csv")).read()
    request_doc = WPS.Execute(
        OWS.Identifier('pandas'),
        WPS.DataInputs(
            WPS.Input(
                OWS.Identifier('csv'),
                WPS.Data(WPS.ComplexData(text, mimeType='text/csv'))
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
    penguins = json.loads(resp.data)
    assert penguins[0]['species'] == "Adelie"


def test_wps_pandas_as_ref():
    client = client_for(Service(processes=[Pandas()]))
    datainputs = "csv=@xlink:href={0}".format(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='pandas',
        datainputs=datainputs,
        rawdataoutput='output=@mimetype=application/json'
    )
    print(resp.data)
    assert resp.status_code == 200
    penguins = json.loads(resp.data)
    assert penguins[0]['species'] == "Adelie"
