#!/usr/bin/env python
'''
This example demonstrates the internal workings of a regular expression lookup.
'''
import pycallgraph
import re


def main():
    pycallgraph.start_trace()
    re.search('(hel[j-s]o).*(th[^e]*ere)', 'hello there')
    pycallgraph.make_dot_graph('regexp.png')

if __name__ == '__main__':
    main()
