from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file
from emu.processes.wps_wordcounter import WordCounter


def test_wps_wordcount():
    client = client_for(Service(processes=[WordCounter()]))
    datainputs = "text=@xlink:href=file://{0}".format(
        resource_file('alice-in-wonderland.txt'))
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='wordcounter',
        datainputs=datainputs)
    assert_response_success(resp)
