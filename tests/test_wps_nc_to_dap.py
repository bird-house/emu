import pytest

from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, get_output
from emu.processes.wps_nc_to_dap import NcToDap
from emu.processes.wps_output_formats import OutputFormats


@pytest.mark.online
def test_wps_nc_to_dap():
    # Create netCDF file on server
    client = client_for(Service(processes=[OutputFormats()]))
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='output_formats',)
    nc_url = get_output(resp.xml)['netcdf']

    # Convert to DAP link
    client = client_for(Service(processes=[NcToDap()]))
    datainputs = "resource=@xlink:href={0}".format(nc_url)
    resp = client.get(
        service='wps', request='execute', version='1.0.0',
        identifier='nc_to_dap',
        datainputs=datainputs)
    assert_response_success(resp)
    assert 'dodsC' in get_output(resp.xml)['dap']


