#!/usr/bin/env python
'''
This example demonstrates the internal workings of a regular expression lookup.
'''
import re

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput


def main():
    graphviz = GraphvizOutput()
    graphviz.output_file = 'regexp.png'
    config = Config(include_stdlib=True)

    with PyCallGraph(output=graphviz, config=config):
        reo = compile()
        match(reo)


def compile():
    return re.compile('^[abetors]*$')


def match(reo):
    [reo.match(a) for a in words()]


def words():
    return [
        'abbreviation',
        'abbreviations',
        'abettor',
        'abettors',
        'abilities',
        'ability',
        'abrasion',
        'abrasions',
        'abrasive',
        'abrasives',
    ]

if __name__ == '__main__':
    main()
