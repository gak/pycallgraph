class Output:

    def __init__(self):
        pass

    def sanity_check(self):
        '''
        Basic checks for certain libraries or external applications. Raise
        or warn if there is a problem.
        '''
        raise NotImplementedError('sanity_check')

    def update(self):
        '''
        If the Output generator allows real-time updates, this method will
        be called periodically during a trace.
        '''
        raise NotImplementedError('update')

    def is_realtime(self):
        '''
        Return True if the update method should be called periodically.
        '''
        return False

    def done(self):
        '''
        Called when the trace is complete and ready to be saved.
        '''
        raise NotImplementedError('done')


