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
This example demonstrates a simple recursive call.
"""

import pycallgraph

pycallgraph.start_trace()


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def main(self):
    for a in xrange(1, 10):
        print factorial(a)

    pycallgraph.make_dot_graph('recursive.png')

if __name__ == '__main__':
    main()

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
