from fnmatch import fnmatch


class Grouper(object):
    '''Group module names.

    By default, objects are grouped by their top-level module name. Additional
    groups can be specified with the groups list and all objects will be
    matched against it.
    '''

    def __init__(self, groups=None):
        if groups is None:
            groups = []

        self.groups = groups

    def __call__(self, full_name=None):
        for pattern in self.groups:
            if fnmatch(full_name, pattern):
                if pattern[-2:] == ".*":
                    # a wilcard in the middle is probably meaningful, while at
                    # the end, it's only noise and can be removed
                    return pattern[:-2]
                return pattern
        return full_name.split('.', 1)[0]
