#!/usr/bin/env python
'''
This example demonstrates the use of filtering.
'''
import pycallgraph


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()

    def secret_function(self):
        pass


def filter_exclude():
    filter_func = pycallgraph.GlobbingFilter(exclude=[
        'pycallgraph.*', '*.secret_function',
    ])
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-exclude.png')


def filter_include():
    filter_func = pycallgraph.GlobbingFilter(include=[
        '*.secret_function', 'Banana.__init__',
    ])
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-include.png')


def filter_max_depth():
    filter_func = pycallgraph.GlobbingFilter(max_depth=1)
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-max-depth.png')


def main():
    filter_exclude()
    filter_include()
    filter_max_depth()

if __name__ == '__main__':
    main()
