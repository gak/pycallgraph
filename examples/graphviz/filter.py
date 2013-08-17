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
        pass


def pycg(name, filter_func):
    config = Config()
    config.filter_func = filter_func
    graphviz = GraphvizOutput()
    graphviz.output_file = 'filter-{}.png'.format(name)
    return PyCallGraph(config=config, outputs=graphviz)

def filter_exclude():
    filter_func = GlobbingFilter(exclude=[
        '*.secret_function',
    ])

    with pycg('exclude', filter_func):
        banana = Banana()
        banana.eat()


def filter_include():
    filter_func = GlobbingFilter(include=[
        '*.secret_function', 'Banana.__init__',
    ])
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-include.png')


def filter_max_depth():
    filter_func = GlobbingFilter(max_depth=1)
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-max-depth.png')


def main():
    filter_exclude()
    # filter_include()
    # filter_max_depth()

if __name__ == '__main__':
    main()
