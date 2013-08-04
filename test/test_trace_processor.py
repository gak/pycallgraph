import sys

from helpers import *
import calls
from pycallgraph.tracer import TraceProcessor


@pytest.fixture
def trace_processor(config):
    return TraceProcessor([], config)


def test_empty(trace_processor):
    sys.settrace(trace_processor.process)
    sys.settrace(None)

    assert trace_processor.call_dict == {}


def test_nop(trace_processor):
    sys.settrace(trace_processor.process)
    calls.nop()
    sys.settrace(None)

    assert trace_processor.call_dict == {
        '__main__': {
            'calls.nop': 1
        }
    }


def test_one_nop(trace_processor):
    sys.settrace(trace_processor.process)
    calls.one_nop()
    sys.settrace(None)

    assert trace_processor.call_dict == {
        '__main__': {'calls.one_nop': 1},
        'calls.one_nop': {'calls.nop': 1},
    }
