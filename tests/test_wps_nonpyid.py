from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, get_output
from emu.processes.wps_nonpyid import NonPyID
import json

def test_wps_nonpyid():
    d = {'a': 1}
    client = client_for(Service(processes=[NonPyID()]))
    datainputs = "input 1=10;input-2={}".format(json.dumps(d))
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='Fake.process-for testing',
        datainputs=datainputs)
    assert_response_success(resp)
    assert get_output(resp.xml) == {'output.1': '11', 'output 2': json.dumps(d)}
