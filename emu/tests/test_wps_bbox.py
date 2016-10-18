import pytest

from pywps import Service

from emu.tests.common import client_for, assert_response_success
from emu.processes.wps_bbox import Box


@pytest.mark.skip(reason="no way of currently testing this")
def test_wps_bbox():
    client = client_for(Service(processes=[Box()]))
    datainputs = "bbox=101,42,110,46"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='bbox',
        datainputs=datainputs)
    assert_response_success(resp)
