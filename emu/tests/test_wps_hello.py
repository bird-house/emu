from pywps import Service

from emu.tests.common import client_for, assert_response_success
from emu.processes.wps_hello import Hello


def test_wps_hello():
    client = client_for(Service(processes=[Hello()]))
    datainputs = "name=LovelySugarBird"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0', identifier='hello',
        datainputs=datainputs)
    assert_response_success(resp)
