#!/usr/bin/env python
'''
This example is trying to make a large graph. You'll need some internet access
for this to work.
'''

import pycallgraph


def main():
    pycallgraph.start_trace()
    import urllib
    from xml.dom.minidom import parse, parseString
    parseString(urllib.urlopen('http://w3.org/').read())
    pycallgraph.make_dot_graph('large.png')

if __name__ == '__main__':
    main()
