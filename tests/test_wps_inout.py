import pytest
import os
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, get_output, resource_file, CFG_FILE
from emu.processes.wps_inout import InOut

NC_FILE_URL = "file://{}".format(resource_file('test.nc'))


def test_wps_inout():
    client = client_for(Service(processes=[InOut()], cfgfiles=[CFG_FILE]))
    datainputs = "string=onetwothree;int=7;float=2.0;boolean=0;text=some string;dataset=@xlink:href={}"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0', identifier='inout',
        datainputs=datainputs.format(NC_FILE_URL))
    assert_response_success(resp)
    out = get_output(resp.xml)
    assert out['text'] == 'some string'
    assert out['dataset'].endswith('.nc')
