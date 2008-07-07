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
This example demonstrates several different methods on colouring your graph.

See U{http://www.graphviz.org/doc/info/attrs.html#k:color} for details on
how to return colour formats to Graphviz.
"""

import random

import pycallgraph


def rainbow(calls, total_time):
    """Colour using only changes in hue.

    It will go from 0 to 0.8 which is red, orange, yellow, green, cyani, blue
    then purple.

    See U{http://en.wikipedia.org/wiki/Hue} for more information on hue.
    """
    return '%f 0.8 0.8' % (calls * 0.8)


def greyscale(calls, total_time):
    """Goes from dark grey to a light grey."""
    return '0 0 %f' % (calls / 2 + 0.4)


def orange_green(calls, total_time):
    """Make a higher total time have an orange colour and a higher number
    of calls have a green colour using RGB.
    """
    return '#%02X%02X%02X' % (
        0x30 + total_time * 0xc0,
        0x30 + calls * 0xc0 + total_time * 0x70,
        0x30,
    )


def rand(calls, total_time):
    """Random with a touch of usefulness"""
    return '%f %f %f' % (
        random.random(),
        calls * 0.5 + 0.5,
        calls * 0.5 + 0.5,
    )


def main():

    # Do the trace, remember the values for later
    pycallgraph.start_trace()
    import HTMLParser
    pycallgraph.stop_trace()

    # Set the edge colour to black for all examples
    pycallgraph.settings['edge_colour'] = lambda a, b: 'black'

    # Default node colouring
    pycallgraph.make_dot_graph('colours-default.png')

    # Rainbow
    pycallgraph.settings['node_colour'] = rainbow
    pycallgraph.make_dot_graph('colours-rainbow.png')

    # Greyscale
    pycallgraph.settings['node_colour'] = greyscale
    pycallgraph.make_dot_graph('colours-greyscale.png')

    # Orange/Green
    pycallgraph.settings['node_colour'] = orange_green
    pycallgraph.make_dot_graph('colours-orange-green.png')

    # Random
    pycallgraph.settings['node_colour'] = rand
    pycallgraph.make_dot_graph('colours-random.png')

if __name__ == '__main__':
    main()

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
