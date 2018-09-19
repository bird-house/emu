import pytest

from pywps import Service
from pywps.tests import client_for, assert_response_success

from .common import get_output
from emu.processes.wps_multiple_outputs import MultipleOutputs


def test_wps_multiple_outputs():
    client = client_for(Service(processes=[MultipleOutputs()]))
    datainputs = "count=2"
    resp = client.get(
        "?service=WPS&request=Execute&version=1.0.0&identifier=multiple_outputs&datainputs={}".format(
            datainputs))
    assert_response_success(resp)
    out = get_output(resp.xml)
    assert 'output' in out.keys()
    assert 'reference' in out.keys()
