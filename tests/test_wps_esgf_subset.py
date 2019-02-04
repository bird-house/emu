import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, resource_file, get_output
from emu.processes.wps_esgf_subset import EmuSubset
import owslib.wps
from owslib import esgfapi

NC_FILE_URL = resource_file('test.nc')

variable = esgfapi.Variable(var_name='meantemp', uri=NC_FILE_URL, name='test')
domain = esgfapi.Domain([
    esgfapi.Dimension('time', 0, 10, crs='indices'),
])


@pytest.mark.online
def test_wps_esgf_subset():
    client = client_for(Service(processes=[EmuSubset()]))
    datainputs = "variable={variable};" \
                 "domain={domain}".format(variable=variable.value, domain=domain.value)
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='emu_subset',
        datainputs=datainputs)
    assert_response_success(resp)
    out = get_output(resp.xml)
    assert out['preview'] != 'plot failed'
