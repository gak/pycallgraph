import pytest
from StringIO import StringIO

import fix_path
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


@pytest.fixture(scope="module")
def pycg():
    return PyCallGraph()


@pytest.fixture(scope="module")
def dot():
    io = StringIO()
    return GraphvizOutput(fp=io)

