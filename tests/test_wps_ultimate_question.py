import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_ultimate_question import UltimateQuestion


@pytest.mark.slow
def test_wps_ultimate_question():
    client = client_for(Service(processes=[UltimateQuestion()]))
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='ultimate_question')
    assert_response_success(resp)
