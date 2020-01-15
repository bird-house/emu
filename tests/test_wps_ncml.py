import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
from emu.processes.wps_ncml import NcMLAgg


@pytest.mark.online
def test_wps_ncml():
    client = client_for(Service(processes=[NcMLAgg()]))

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='ncml')
    print(resp.response)
    assert_response_success(resp)
