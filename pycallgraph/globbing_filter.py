class GlobbingFilter(object):

    '''Filter module names using a set of globs.

    Objects are matched against the exclude list first, then the include list.
    Anything that passes through without matching either, is excluded.
    '''

    def __init__(self, include=None, exclude=None, max_depth=None,
                 min_depth=None, fraction=None):
        if include is None and exclude is None:
            include = ['*']
            exclude = []
        elif include is None:
            include = ['*']
        elif exclude is None:
            exclude = []
        self.include = include
        self.exclude = exclude
        if max_depth is None:
           self.max_depth = max_depth or 9999
        else:
           self.max_depth = max_depth
        if min_depth is None:
            self.min_depth = 0
        else:
            self.min_depth = min_depth or 0
        if fraction is None:
            self.fraction = 0
        else:
            self.fraction = fraction

    def __call__(self, stack, module_name=None, class_name=None,
                 func_name=None, full_name=None):
        from fnmatch import fnmatch
        if len(stack) > self.max_depth:
            return False
        if len(stack) < self.min_depth:
            return False
        for pattern in self.exclude:
            if fnmatch(full_name, pattern):
                return False
        for pattern in self.include:
            if fnmatch(full_name, pattern):
                return True
        return False


