#!/usr/bin/env python
'''
This example demonstrates the use of filtering.
'''
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()

    def secret_function(self):
        time.sleep(0.2)


def pycg(name, trace_filter, comment=None):
    config = Config()
    config.trace_filter = trace_filter

    graphviz = GraphvizOutput()
    graphviz.output_file = 'filter-{}.png'.format(name)
    if comment:
        graphviz.graph_attributes['graph']['label'] = comment

    return PyCallGraph(config=config, outputs=graphviz)


def filter_exclude():
    trace_filter = GlobbingFilter(exclude=[
        'pycallgraph.*',
        '*.secret_function',
    ])

    with pycg('exclude', trace_filter, 'Should not include secret_function.'):
        banana = Banana()
        banana.eat()


def filter_include():
    trace_filter = GlobbingFilter(include=[
        '*.secret_function',
        'Banana.eat',
    ])
    with pycg('include', trace_filter, 'Should show secret_function.'):
        banana = Banana()
        banana.eat()


def filter_include():
    trace_filter = GlobbingFilter(include=[
        '*.secret_function',
        'Banana.eat',
    ])
    with pycg('include', trace_filter, 'Should show secret_function.'):
        banana = Banana()
        banana.eat()


def main():
    filter_exclude()
    filter_include()


if __name__ == '__main__':
    main()
