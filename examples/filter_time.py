#!/usr/bin/env python
"""
pycallgraph

U{http://pycallgraph.slowchop.com/}

Copyright Gerald Kaszuba 2007

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

"""
This example demonstrates the use of filtering timing functionality.
"""
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

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
