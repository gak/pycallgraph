import json

from helpers import *
from calls import *


@pytest.fixture
def jsono(temp):
    g = JsonOutput()
    g.output_file = temp
    return g


def test_simple(jsono):
    with PyCallGraph(output=jsono):
        one_nop()
    d = json.load(open(jsono.output_file))
    os.unlink(jsono.output_file)

    assert 'nodes' in d
    assert 'edges' in d
    assert 'groups' in d
    assert 'calls.one_nop' in d['nodes']
    assert 'calls' in d['groups']
    assert len(d['edges']) is 2
