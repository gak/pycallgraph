try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import time

from helpers import *


@pytest.fixture(scope='module')
def pycg():
    return PyCallGraph()


@pytest.fixture(scope='module')
def config():
    return Config()


@pytest.fixture(scope='module')
def graphviz_source():
    output = GraphvizOutput()
    output.fp = StringIO()
    return output


@pytest.fixture(scope='module')
def pickle_output():
    output = PickleOutput()
    output.fp = StringIO()
    return output
