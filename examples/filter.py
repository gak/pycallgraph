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
This example demonstrates the use of filtering.
"""
import pycallgraph


class Banana:

    def __init__(self):
        pass

    def eat(self):
        self.secret_function()

    def secret_function(self):
        pass


def filter_exclude():
    filter_func = pycallgraph.GlobbingFilter(exclude=['pycallgraph.*', \
        '*.secret_function'])
    pycallgraph.start_trace(filter_func=filter_func)
    banana = Banana()
    banana.eat()
    pycallgraph.make_dot_graph('filter-exclude.png')


def filter_include():
    filter_func = pycallgraph.GlobbingFilter(include=['*.secret_function', \
        'Banana.__init__'])
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

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
