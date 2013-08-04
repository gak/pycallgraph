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
