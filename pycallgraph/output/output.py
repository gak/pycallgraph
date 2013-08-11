import re
import os
from distutils.spawn import find_executable

from ..exceptions import PyCallGraphException


class Output(object):
    '''Base class for all outputters.'''

    def sanity_check(self):
        '''Basic checks for certain libraries or external applications.  Raise
        or warn if there is a problem.
        '''
        pass

    @classmethod
    def add_arguments(cls, subparsers):
        pass

    def reset(self):
        pass

    def set_processor(self, processor):
        self.processor = processor

    def start(self):
        '''Initialise variables after initial configuration.'''
        pass

    def update(self):
        '''Called periodically during a trace, but only when should_update is
        set to True.
        '''
        raise NotImplementedError('update')

    def should_update(self):
        '''Return True if the update method should be called periodically.'''
        return False

    def done(self):
        '''Called when the trace is complete and ready to be saved.'''
        raise NotImplementedError('done')

    def ensure_binary(self, cmd):
        if find_executable(cmd):
            return

        raise PyCallGraphException(
            'The command "{}" is required to be in your path.'.format(cmd))

    def normalize_path(self, path):
        regex_user_expand = re.compile('\A~')
        if regex_user_expand.match(path):
            path = os.path.expanduser(path)
        else:
            path = os.path.expandvars(path)  # expand, just in case
        return path

    def prepare_output_file(self):
        if self.fp is None:
            self.output_file = self.normalize_path(self.output_file)
            self.fp = open(self.output_file, 'wb')

    def human_readable_size(self, num):
        for x in ['B', 'KB', 'MB', 'GB']:
            if num < 1024.0 and num > -1024.0:
                return "%3.1f%s" % (num, x)
            num /= 1024.0
        return "%3.1f%s" % (num, 'TB')

    @classmethod
    def add_output_file(cls, subparser, defaults, help):
        subparser.add_argument(
            '-o', '--output-file', type=str, default=defaults.output_file,
            help=help,
        )
