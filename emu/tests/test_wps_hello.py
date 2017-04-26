from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_say_hello import SayHello


def test_wps_hello():
    client = client_for(Service(processes=[SayHello()]))
    datainputs = "name=LovelySugarBird"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0', identifier='hello',
        datainputs=datainputs)
    assert_response_success(resp)
