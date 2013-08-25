#!/usr/bin/env python
'''
This example demonstrates a simple use of pycallgraph.
'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GephiOutput


class Banana:

    def eat(self):
        pass


class Person:

    def __init__(self):
        self.no_bananas()

    def no_bananas(self):
        self.bananas = []

    def add_banana(self, banana):
        self.bananas.append(banana)

    def eat_bananas(self):
        [banana.eat() for banana in self.bananas]
        self.no_bananas()


def main():
    gephi = GephiOutput()
    gephi.output_file = 'basic.gdf'

    with PyCallGraph(output=gephi):
        person = Person()
        for a in xrange(10):
            person.add_banana(Banana())
        person.eat_bananas()


if __name__ == '__main__':
    main()
