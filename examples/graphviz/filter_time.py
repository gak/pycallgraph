#!/usr/bin/env python
'''
This example demonstrates the use of filtering timing functionality.
'''
import re

import pycallgraph


def filter_none():
    pycallgraph.start_trace()
    for a in xrange(100):
        re.compile('test1-%i' % a)
    pycallgraph.make_dot_graph('filter-time-none.png')


def filter_min_depth():
    filter_func = pycallgraph.GlobbingFilter(min_depth=7)
    pycallgraph.start_trace(time_filter_func=filter_func)
    for a in xrange(100):
        re.compile('test2-%i' % a)
    pycallgraph.make_dot_graph('filter-time-min-depth.png')


def filter_module():
    filter_func = pycallgraph.GlobbingFilter(include=['sre_parse.*'])
    pycallgraph.start_trace(time_filter_func=filter_func)
    for a in xrange(100):
        re.compile('test3-%i' % a)
    pycallgraph.make_dot_graph('filter-time-module.png')


def main():
    filter_none()
    filter_min_depth()
    filter_module()

if __name__ == '__main__':
    main()
