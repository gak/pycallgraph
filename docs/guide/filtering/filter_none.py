#!/usr/bin/env python

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

from banana import Banana


graphviz = GraphvizOutput(output_file='filter_none.png')

with PyCallGraph(output=graphviz):
    banana = Banana()
    banana.eat()
