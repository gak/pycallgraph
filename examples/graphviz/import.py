#!/usr/bin/env python
'''
This example shows the interals of certain Python modules when they are being
imported.
'''
from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput


def main():
    import_list = (
        'pickle',
        'htmllib',
        'urllib2',
    )
    graphviz = GraphvizOutput()
    config = Config(include_stdlib=True)

    for module in import_list:
        graphviz.output_file = 'import-{}.png'.format(module)
        with PyCallGraph(output=graphviz, config=config):
            __import__(module)


if __name__ == '__main__':
    main()
