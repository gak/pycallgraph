from helpers import *
from pycallgraph.output import GraphvizOutput
from pycallgraph import pycall_profile

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

@pycall_profile()
def print_something():
    print "hello"


def test_wrapper():
    print_something()


if __name__ == "__main__":
    test_wrapper()
