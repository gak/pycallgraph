#!/usr/bin/env python
'''
This example demonstrates a simple use of pycallgraph.
'''

import pycallgraph


class Banana:

    def __init__(self):
        pass

    def eat(self):
        pass


def main():
    pycallgraph.start_trace()
    banana = Banana()
    banana.eat()
    pycallgraph.make_gdf_graph('basic.gdf')

if __name__ == '__main__':
    main()
