#!/usr/bin/env python
'''
This example demonstrates the use of grouping.
'''
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph import Grouper
from pycallgraph.output import GraphvizOutput
import example_with_submodules


def run(name, trace_grouper=None, config=None, comment=None):
    if not config:
        config = Config()

    config.trace_filter = GlobbingFilter()

    if trace_grouper is not None:
        config.trace_grouper = trace_grouper

    graphviz = GraphvizOutput()
    graphviz.output_file = 'grouper-{}.png'.format(name)
    if comment:
        graphviz.graph_attributes['graph']['label'] = comment

    with PyCallGraph(config=config, output=graphviz):
        example_with_submodules.main()


def group_none():
    run(
        'without',
        comment='Default grouping.'
    )


def group_some():
    trace_grouper = Grouper(groups=[
        'example_with_submodules.submodule_one.*',
        'example_with_submodules.submodule_two.*',
        'example_with_submodules.helpers.*',
    ])

    run(
        'with',
        trace_grouper=trace_grouper,
        comment='Should assign groups to the two submodules.',
    )


def group_methods():
    trace_grouper = Grouper(groups=[
        'example_with_submodules.*.report',
        ])

    run(
        'methods',
        trace_grouper=trace_grouper,
        comment='Should assign a group to the report methods.',
    )


def main():
    group_none()
    group_some()
    group_methods()


if __name__ == '__main__':
    main()
