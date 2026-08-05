import os
import pathlib

from pywps import get_ElementMakerForVersion
from pywps.app.basic import get_xpath_ns
from pywps.tests import WpsClient, WpsTestResponse

TESTS_HOME = str(pathlib.Path(__file__).parent.resolve())
CFG_FILE = str(pathlib.Path(TESTS_HOME).joinpath('test.cfg'))

VERSION = "1.0.0"
WPS, OWS = get_ElementMakerForVersion(VERSION)
xpath_ns = get_xpath_ns(VERSION)


def resource_file(filepath):
    return str(pathlib.Path(TESTS_HOME).joinpath('testdata', filepath))


class WpsTestClient(WpsClient):

    def get(self, *args, **kwargs):  # noqa: F841
        query = "?"
        for key, value in kwargs.items():
            query += f"{key}={value}&"
        return super().get(query)


def client_for(service):
    return WpsTestClient(service, WpsTestResponse)


def get_output(doc):
    """Copied from pywps/tests/test_execute.py."""
    # TODO: make this helper method public in pywps
    output = {}
    for output_el in xpath_ns(doc, "/wps:ExecuteResponse" "/wps:ProcessOutputs/wps:Output"):
        [identifier_el] = xpath_ns(output_el, "./ows:Identifier")

        lit_el = xpath_ns(output_el, './wps:Data/wps:LiteralData')
        if lit_el:
            output[identifier_el.text] = lit_el[0].text

        ref_el = xpath_ns(output_el, './wps:Reference')
        if ref_el:
            output[identifier_el.text] = ref_el[0].attrib['href']

        data_el = xpath_ns(output_el, './wps:Data/wps:ComplexData')
        if data_el:
            output[identifier_el.text] = data_el[0].text

    return output
