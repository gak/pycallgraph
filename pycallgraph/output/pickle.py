try:
    import cPickle as pickle
except ImportError:
    import pickle

from .output import Output


class PickleOutput(Output):

    def __init__(self):
        self.fp = None
        self.output_file = 'pycallgraph.dot'

    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()

        subparser = subparsers.add_parser(
            'pickle',
            help='Dump to a cPickle file for generation later',
            parents=[parent_parser], usage=usage,
        )

        subparser.add_argument(
            '-o', '--output-file', type=str, default=defaults.output_file,
            help='The generated cPickle file',
        )

    def done(self):
        self.prepare_output_file()
        pickle.dump(self.tracer, self.fp, pickle.HIGHEST_PROTOCOL)
