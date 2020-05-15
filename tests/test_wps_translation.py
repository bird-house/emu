from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, CFG_FILE
from emu.processes.wps_translation import Translation


def test_wps_translation_describe_fr():
    client = client_for(Service(processes=[Translation()], cfgfiles=CFG_FILE))
    resp = client.get(
        service='wps', request='DescribeProcess', version='1.0.0',
        identifier='translation',
        language="fr-CA")
    print(resp.data)
    title = resp.xpath_text(
        '/wps:ProcessDescriptions'
        '/ProcessDescription'
        '/ows:Title'
    )
    assert title == 'Processus traduit'


def test_wps_translation_describe_de():
    client = client_for(Service(processes=[Translation()], cfgfiles=CFG_FILE))
    resp = client.get(
        service='wps', request='DescribeProcess', version='1.0.0',
        identifier='translation',
        language="de-DE")
    print(resp.data)
    title = resp.xpath_text(
        '/wps:ProcessDescriptions'
        '/ProcessDescription'
        '/ows:Title'
    )
    assert title == 'Mehrsprachiger Prozess'


def test_wps_translation_execute():
    client = client_for(Service(processes=[Translation()], cfgfiles=CFG_FILE))
    datainputs = "input1=10"
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='translation',
        datainputs=datainputs,
        language="fr-CA")
    print(resp.data)
    assert_response_success(resp)

    outputs = list(resp.xpath('/wps:ExecuteResponse/wps:ProcessOutputs/wps:Output')[0])
    assert outputs[1].text == "Sortie #1"
