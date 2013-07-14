import pytest
from StringIO import StringIO
import time

import fix_path
from pycallgraph import *
from pycallgraph.output import *


@pytest.fixture(scope='module')
def pycg():
    return PyCallGraph()

@pytest.fixture(scope='module')
def config():
    return Config()

@pytest.fixture(scope='module')
def graphviz_source():
    output = GraphvizSourceOutput()
    output.fp = StringIO()
    return output

@pytest.fixture(scope='module')
def graphviz_image():
    output = GraphvizImageOutput()
    output.fp = StringIO()
    return output

@pytest.fixture(scope='module')
def pickle_output():
    output = PickleOutput()
    output.fp = StringIO()
    return output


	