from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, CFG_FILE
from emu.processes.wps_output_formats import OutputFormats


def test_wps_output_formats():
    client = client_for(Service(processes=[OutputFormats()], cfgfiles=CFG_FILE))
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='output_formats',)
    assert_response_success(resp)
