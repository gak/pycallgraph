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
    def inject_config(cls, config):
        pass

    @classmethod
    def add_arguments(cls, subparsers):
        pass

    def update(self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        :
        '''
        If the Output g                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             enerator allows real-time updates, this method will
        be called periodically during a trace.
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
