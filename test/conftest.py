from helpers import *


@pytest.fixture(scope='module')
def pycg():
    return PyCallGraph()


@pytest.fixture(scope='module')
def config():
    return Config()
