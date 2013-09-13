#!/usr/bin/env python
'''
This example is trying to make a large graph. You'll need some internet access
for this to work.
'''

from pycallgraph import PyCallGraph
from pycallgraph.output import JsonOutput


def main():
    json = JsonOutput()
    json.output_file = 'large.json'

    with PyCallGraph(output=json):
        from urllib2 import urlopen
        from xml.dom.minidom import parseString
        parseString(urlopen('http://w3.org/').read())


if __name__ == '__main__':
    main()
