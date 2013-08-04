#!/usr/bin/env python
'''
This example demonstrates a simple recursive call.
'''

import pycallgraph


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def main():
    pycallgraph.start_trace()
    for a in xrange(1, 10):
        factorial(a)

    pycallgraph.make_dot_graph('recursive.png')

if __name__ == '__main__':
    main()
