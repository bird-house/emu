import pytest

from pywps import Service
from pywps.tests import assert_response_success
from emu.processes.wps_ncml import NcMLAgg
from .common import client_for, CFG_FILE
# from owslib.wps import WPSExecution


@pytest.mark.online
def test_wps_ncml():

    client = client_for(Service(processes=[NcMLAgg()], cfgfiles=CFG_FILE))

    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='ncml')

    assert_response_success(resp)

    # ex = WPSExecution()
    # ex.parseResponse(resp.xml)
    # d1, d2, d3 = ex.processOutputs
    # ncml = d3.retrieveData()
    # assert ncml.strip().startswith("<")


