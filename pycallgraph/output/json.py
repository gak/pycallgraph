# To be able to import json without import this module :)
# Found on http://stackoverflow.com/a/13714762/11125
from importlib import import_module
json = import_module('json')

from .output import Output


class JsonOutput(Output):

    def __init__(self):
        self.fp = None
        self.output_file = 'pycallgraph.json'

    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()

        subparser = subparsers.add_parser(
            'json',
            help='Dump trace to a JSON file',
            parents=[parent_parser], usage=usage,
        )

        subparser.add_argument(
            '-o', '--output-file', type=str, default=defaults.output_file,
            help='The generated JSON file',
        )

        return subparser

    def done(self):
        self.prepare_output_file()

        nodes = []
        for node in self.processor.nodes():
            item = {}
            for k, v in node.__dict__.iteritems():
                if hasattr(v, '__dict__'):
                    item[k] = v.__dict__
                else:
                    item[k] = v


            nodes.append(item)

        out = {
            'nodes': nodes,
        }

        json.dump(out, self.fp)
