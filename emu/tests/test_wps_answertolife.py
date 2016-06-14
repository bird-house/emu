import pytest

from emu.tests.common import WpsTestClient, assert_response_success

@pytest.mark.slow
def test_wps_ultimatequestionprocess():
    wps = WpsTestClient()
    resp = wps.get(service='wps', request='execute', version='1.0.0', identifier='ultimatequestionprocess')
    assert_response_success(resp)
