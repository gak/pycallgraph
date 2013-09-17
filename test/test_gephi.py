from helpers import *
from calls import *


@pytest.fixture
def gephi(temp):
    g = GephiOutput()
    g.output_file = temp
    return g


def test_simple(gephi):
    with PyCallGraph(output=gephi):
        one_nop()
    generated = open(gephi.output_file).read()
    os.unlink(gephi.output_file)

    assert 'nodedef> name VARCHAR' in generated
    assert 'edgedef> node1 VARCHAR, node2 VARCHAR' in generated
    assert 'calls.one_nop,calls.one_nop,calls,1' in generated
    assert 'calls.one_nop,calls.nop,1' in generated
