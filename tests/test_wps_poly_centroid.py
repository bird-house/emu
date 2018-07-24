import pytest
import os
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for
import emu
from emu.processes.wps_poly_centroid import PolyCentroid
from eggshell.config import Paths

paths = Paths(emu)
TESTS_HOME = os.path.abspath(os.path.dirname(__file__))
cfgfiles = os.path.join(TESTS_HOME, 'test.cfg')

def test_wps_poly_centroid():
    client = client_for(Service(processes=[PolyCentroid(), ], cfgfiles=cfgfiles))
    fn = os.path.join(TESTS_HOME, 'testdata', 'poly.xml')
    datainputs = "polygon=files@xlink:href=file://{0}".format(fn)
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0',
        identifier='poly_centroid',
        datainputs=datainputs)
    assert_response_success(resp)
