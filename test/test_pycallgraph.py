from helpers import *


def test_start_no_outputs():
    pycg = PyCallGraph()
    with pytest.raises(PyCallGraphException):
        pycg.start()


def test_with_block_no_outputs():
    with pytest.raises(PyCallGraphException):
        with PyCallGraph():
            pass
