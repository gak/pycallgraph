from helpers import helper


class SubmoduleTwo(object):
    def __init__(self):
        self.two = 2

    def report(self):
        return helper(self.two)
