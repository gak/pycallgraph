#!/usr/bin/env python
'''
This example demonstrates the use of filtering.
'''
import time

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()
        self.chew()
        self.swallow()

    def secret_function(self):
        time.sleep(0.2)

    def chew(self):
        pass

    def swallow(self):
        pass


def run(name, trace_filter=None, config=None, comment=None):
    if not config:
        config = Config()

    if trace_filter:
        config.trace_filter = trace_filter

    graphviz = GraphvizOutput()
    graphviz.output_file = 'filter-{}.png'.format(name)
    if comment:
        graphviz.graph_attributes['graph']['label'] = comment

    with PyCallGraph(config=config, output=graphviz):
        banana = Banana()
        banana.eat()


def filter_none():
    run(
        'none',
        comment='Default filtering.'
    )


def filter_exclude():
    trace_filter = GlobbingFilter(exclude=[
        'pycallgraph.*',
        '*.secret_function',
    ])

    run(
        'exclude',
        trace_filter=trace_filter,
        comment='Should not include secret_function.',
    )


def filter_include():
    trace_filter = GlobbingFilter(include=[
        '*.secret_function',
        'Banana.eat',
    ])

    run(
        'include',
        trace_filter=trace_filter,
        comment='Should show secret_function.'
    )


def filter_depth():
    config = Config()
    config.max_depth = 1

    run(
        'max_depth',
        config=config,
        comment='Should only show a depth of one.'
    )


def filter_pycallgraph():
    trace_filter = GlobbingFilter(exclude=[])

    run(
        'pycallgraph',
        trace_filter=trace_filter,
        comment="Don't filter pycallgraph calls.",
    )


def main():
    filter_none()
    filter_exclude()
    filter_include()
    filter_depth()
    filter_pycallgraph()


if __name__ == '__main__':
    main()
