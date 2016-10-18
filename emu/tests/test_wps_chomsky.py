from pywps import Service

from emu.tests.common import client_for, assert_response_success
from emu.processes.wps_chomsky import Chomsky


def test_wps_chomsky():
    client = client_for(Service(processes=[Chomsky()]))
    datainputs = "times=10"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='chomsky',
        datainputs=datainputs)
    assert_response_success(resp)
