class Output:

    def __init__(self, config):
        self.config = config

    def sanity_check(self):
        '''
        Basic checks for certain libraries or external applications.  Raise
        or warn if there is a problem.
        '''
        raise NotImplementedError('sanity_check')

    @classmethod
    def add_arguments(cls, subparsers):
        pass

    def reset(self):
        pass

    def set_tracer(self, tracer):
        self.tracer = tracer

    def update(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        :
        '''
        Called periodically during a trace.
        '''
        raise NotImplementedError('update')

    def should_update(self):
        '''
        Return True if the update method should be called periodically.
        '''
        return False

    def done(self):
        '''
        Called when the trace is complete and ready to be saved.
        '''
        raise NotImplementedError('done')
