import pytest
from StringIO import StringIO

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
def dot(config):
    return GraphvizOutput(config)
