#!/usr/bin/env python
'''
This example demonstrates several different methods on colouring your graph.

See U{http://www.graphviz.org/doc/info/attrs.html#k:color} for details on
how to return colour formats to Graphviz.
'''
import random

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import Color
from pycallgraph.output import GraphvizOutput


def rainbow(node):
    '''Colour using only changes in hue.

    It will go from 0 to 0.8 which is red, orange, yellow, green, cyan, blue,
    then purple.

    See http://en.wikipedia.org/wiki/Hue for more information on hue.
    '''
    return Color.hsv(node.time.fraction * 0.8, 0.4, 0.9)


def greyscale(node):
    '''Goes from dark grey to a light grey.'''
    return Color.hsv(0, 0, node.time.fraction / 2 + 0.4)


def orange_green(node):
    '''Make a higher total time have an orange colour and a higher number
    of calls have a green colour using RGB.
    '''
    return Color(
        0.2 + node.time.fraction * 0.8,
        0.2 + node.calls.fraction * 0.4 + node.time.fraction * 0.4,
        0.2,
    )


def rand(node):
    return Color.hsv(
        random.random(),
        node.calls.fraction * 0.5 + 0.5,
        node.calls.fraction * 0.5 + 0.5,
    )


def main():
    graphviz = GraphvizOutput()
    pycallgraph = PyCallGraph(
        output=graphviz,
        config=Config(include_stdlib=True)
    )

    pycallgraph.start()
    import HTMLParser  # noqa
    pycallgraph.stop()

    # Set the edge colour to black for all examples
    graphviz.edge_color_func = lambda e: Color(0, 0, 0)

    # Default node colouring
    graphviz.output_file = 'colours-default.png'
    graphviz.done()

    def run(func, output_file):
        graphviz.node_color_func = func
        graphviz.output_file = output_file
        graphviz.done()

    run(rainbow, 'colors-rainbow.png')
    run(greyscale, 'colors-greyscale.png')
    run(orange_green, 'colors-orange-green.png')
    run(rand, 'colors-random.png')


if __name__ == '__main__':
    main()
