from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_chomsky import Chomsky


def test_wps_chomsky():
    client = client_for(Service(processes=[Chomsky()]))
    datainputs = f"times={10}"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='chomsky',
        datainputs=datainputs)
    assert_response_success(resp)
