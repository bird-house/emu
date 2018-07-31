from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, get_output
from emu.processes.wps_dummy import Dummy


def test_wps_dummy():
    client = client_for(Service(processes=[Dummy()]))
    datainputs = "input1=10;input2=2"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='dummyprocess',
        datainputs=datainputs)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output1': '11', 'output2': '1'}
