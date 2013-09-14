#!/usr/bin/env python
import re

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'regexp.png'

    with PyCallGraph(output=graphviz):
        match(re.compile('^....$'))
        match(re.compile('^[asdfjkl;]*$'))


def match(reo):
    for w in open('/usr/share/dict/words'):
        reo.match(w)


if __name__ == '__main__':
    main()
