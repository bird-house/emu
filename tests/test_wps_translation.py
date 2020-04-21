from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_translation import Translation


def test_wps_translation_execute():
    client = client_for(Service(processes=[Translation()]))
    datainputs = "input1=10"
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='translation',
        datainputs=datainputs,
        language="en-US")
    print(resp.data)
    assert_response_success(resp)

    # outputs = list(resp.xpath('/wps:ExecuteResponse/wps:ProcessOutputs/wps:Output')[0])
    # assert outputs[1].text == "Sortie #1"
