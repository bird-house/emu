import pytest
import json
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file, get_output, CFG_FILE
from emu.processes.wps_wordcounter import WordCounter


def test_wps_wordcount_file():
    client = client_for(Service(processes=[WordCounter()], cfgfiles=[CFG_FILE]))
    datainputs = "text=@xlink:href=file://{0}".format(
        resource_file('alice-in-wonderland.txt'))
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='wordcounter',
        datainputs=datainputs)
    # print(resp.get_data())
    assert_response_success(resp)


@pytest.mark.online
def test_wps_wordcount_href():
    client = client_for(Service(processes=[WordCounter()]))
    datainputs = "text=@xlink:href={0}".format(
        "https://en.wikipedia.org/wiki/Web_Processing_Service")
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='wordcounter',
        datainputs=datainputs,
        rawdataoutput='output=@mimetype=application/json'
    )

    assert resp.status_code == 200
    json.loads(resp.data)
