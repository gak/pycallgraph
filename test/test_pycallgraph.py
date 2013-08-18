from helpers import *


def test_start_no_outputs(pycg):
    with pytest.raises(PyCallGraphException):
        pycg.start()


def test_with_block_no_outputs(pycg):
    with pytest.raises(PyCallGraphException):
        with pycg:
            pass


def test_get_tracer_class(pycg):
    pycg.config.threaded = True
    assert pycg.get_tracer_class() == AsyncronousTracer

    pycg.config.threaded = False
    assert pycg.get_tracer_class() == SyncronousTracer
