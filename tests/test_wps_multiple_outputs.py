import pytest
from pywps import Service
from pywps.tests import assert_response_success

from .common import get_output, client_for, CFG_FILE
from emu.processes.wps_multiple_outputs import MultipleOutputs


@pytest.fixture
def resp():
    client = client_for(Service(processes=[MultipleOutputs()], cfgfiles=CFG_FILE))
    datainputs = f'count={5}'
    response = client.get(
        service="WPS", request="Execute", version="1.0.0", identifier="multiple_outputs",
        datainputs=datainputs)
    return response


def test_wps_multiple_output(resp):
    assert_response_success(resp)
    out = get_output(resp.xml)
    assert 'output' in out


def test_metalink_download(resp):
    md = pytest.importorskip('metalink.download')
    out = get_output(resp.xml)
    d = md.get(out['output'], path='/tmp')
    assert len(d) == 5
