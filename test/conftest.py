import tempfile

from helpers import *


@pytest.fixture(scope='module')
def pycg():
    return PyCallGraph()


@pytest.fixture(scope='module')
def config():
    return Config()


@pytest.fixture(scope='module')
def temp():
    return tempfile.mkstemp()[1]
