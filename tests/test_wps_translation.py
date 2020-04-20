from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_translation import Translation


def test_wps_translation_getcapabilities():
    client = client_for(Service(processes=[Translation()]))
    resp = client.get(service="wps", request="getCapabilities", version="1.0.0", identifier="translation",
                      language="fr-CA")
    assert resp.xpath('/wps:Capabilities/@xml:lang')[0] == "fr-CA"

    supported = resp.xpath('/wps:Capabilities/wps:Languages/wps:Supported/ows:Language/text()')
    assert supported == ["en-US", "fr-CA"]

    processes = list(resp.xpath('//wps:ProcessOfferings')[0])
    assert [e.text for e in processes[0]][:3] == ["translation", "Processus traduit", "Processus incluant des "
                                                                                     "traductions"]

def test_wps_translation_execute():
    client = client_for(Service(processes=[Translation()]))
    datainputs = "input1=10"
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='translation',
        datainputs=datainputs,
        language="fr-CA")
    assert_response_success(resp)

    outputs = list(resp.xpath('/wps:ExecuteResponse/wps:ProcessOutputs/wps:Output')[0])
    assert outputs[1].text == "Sortie #1"




