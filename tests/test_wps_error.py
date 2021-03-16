from pywps import Service
from pywps.tests import client_for

from emu.processes.wps_error import ShowError


def test_wps_error():
    client = client_for(Service(processes=[ShowError()]))
    datainputs = "message=tomorrow-is-another-day;nice=true"
    client.get(
        f"?service=WPS&request=Execute&version=1.0.0&identifier=hello&datainputs={datainputs}"
    )
    # TODO: parse ows:Exception
    # assert_response_success(resp)
    # assert get_output(resp.xml) == {'output': "Hello LovelySugarBird"}
