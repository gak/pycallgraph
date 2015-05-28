import pytest

import pycallgraph
from pycallgraph import PyCallGraphException
from pycallgraph.output import GephiOutput, GraphvizOutput


@pycallgraph.decorators.trace(output=GraphvizOutput())
def print_something():
    print("hello")


@pycallgraph.decorators.trace(output=GephiOutput())
def print_foo():
    print("foo")


@pycallgraph.decorators.trace()
def print_bar():
    print("bar")


def test_trace_decorator_graphviz_output():
    print_something()


def test_trace_decorator_gephi_output():
    print_foo()


def test_trace_decorator_parameter():
    with pytest.raises(PyCallGraphException):
        print_bar()


if __name__ == "__main__":
    test_trace_decorator_graphviz_output()
    test_trace_decorator_gephi_output()
    test_trace_decorator_parameter()
