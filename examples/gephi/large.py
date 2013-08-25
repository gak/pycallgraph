#!/usr/bin/env python
'''
This example is trying to make a large graph. You'll need some internet access
for this to work.
'''

from pycallgraph import PyCallGraph
from pycallgraph.output import GephiOutput


def main():
    gephi = GephiOutput()
    gephi.output_file = 'large.gdf'

    with PyCallGraph(output=gephi):
        from urllib2 import urlopen
        from xml.dom.minidom import parseString
        parseString(urlopen('http://w3.org/').read())


if __name__ == '__main__':
    main()
