import warnings
import sys
import argparse

from .output import outputters


class Config(object):
    '''Handles configuration settings for pycallgraph and each output module.
    It also handles command line arguments.
    '''

    def __init__(self):
        self.output = None
        self.quiet = False
        self.threaded = False
        self.include_stdlib = True
        self.track_memory = False

        self.create_parser()

    def add_module_arguments(self, usage):
        subparsers = self.parser.add_subparsers(
            help='OUTPUT_TYPE', dest='output')
        parent_parser = self.create_parent_parser()

        for name, cls in outputters.iteritems():
            cls.add_arguments(subparsers, parent_parser, usage)

    def get_output(self):
        if not self.output:
            return
        output = outputters[self.output]()
        warnings.warn('output not configured')
        return output

    def parse_args(self, args=None):
        self.parser.parse_args(args, namespace=self)

    def create_parser(self):
        '''Used by the pycallgraph command line interface to parse
        arguments.
        '''
        usage = 'pycallgraph [options] OUTPUT_TYPE [output_options] -- ' \
            'SCRIPT.py [ARG ...]'

        self.parser = argparse.ArgumentParser(
            description='Python Call Graph profiles a Python script and '
            'generates a call graph visualisation.', usage=usage,
        )

        self.add_ungrouped_arguments()
        self.add_filter_arguments()
        self.add_module_arguments(usage)

    def create_parent_parser(self):
        '''Mixing subparsers with positional arguments can be done with a
        parents option. Found via: http://stackoverflow.com/a/11109863/11125
        '''
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument(
            'command', metavar='SCRIPT',
            help='The Python script file to profile',
        )
        parent_parser.add_argument(
            'command_args', metavar='ARG', nargs='*',
            help='Python script arguments.'
        )
        return parent_parser

    def add_ungrouped_arguments(self):
        self.parser.add_argument(
            '-q', '--quiet', dest='quiet', action='store_true',
            help='Suppress status output to the console')

        self.parser.add_argument(
            '-t', '--threaded', action='store_true',
            help='Process traces asyncronously')

        self.parser.add_argument(
            '-s', '--stdlib', dest='include_stdlib', action='store_true',
            default=self.include_stdlib,
            help='Include standard library functions in the trace')

        self.parser.add_argument(
            '-m', '--track-memory', dest='track_memory', action='store_true',
            default=self.track_memory,
            help='(Experimental) Track memory usage')

    def add_filter_arguments(self):
        group = self.parser.add_argument_group('filtering')
        group.add_argument(
            '-i', '--include', dest='include', default=[], action='append',
            help='Wildcard pattern of modules to include in the output. '
            'You can have multiple include arguments.'
        )

        group.add_argument(
            '-e', '--exclude', dest='exclude', default=[], action='append',
            help='Wildcard pattern of modules to exclude in the output. '
            'You can have multiple exclude arguments.'
        )

        group.add_argument(
            '-d', '--max-depth', dest='max_depth', default=None,
            help='Maximum stack depth to trace')

        group.add_argument(
            '--include-timing', dest='include_timing', default=[],
            action='append',
            help='Wildcard pattern of modules to include in time measurement. '
            'You can have multiple include arguments.',
        )

        group.add_argument(
            '--exclude-timing', dest='exclude_timing', default=[],
            action='append',
            help='Wildcard pattern of modules to exclude in time '
            'measurement. You can have multiple exclude arguments.',
        )

        group.add_argument(
            '--time_fraction_threshhold', dest='time_fraction_threshhold',
            default=0.05,
            help='Set a threshhold for inclusion of functions '
            'in graphical output in terms of fraction of total time used.',
        )
