import pycallgraph


class CommandLine(object):
    '''Used for the preparation of the command-line script.
    '''

    def __init__(self):
        self.config = pycallgraph.Config()

    def parse_args(self):
        self.config.parse_args()

        # Create filter
        if not self.config.include:
            self.config.include = ['*']
        filter_func = pycallgraph.GlobbingFilter(
            include=self.config.include,
            exclude=self.config.exclude,
            max_depth=self.config.max_depth,
            )

        # Create timing filter
        if not self.config.include_timing:
            self.config.include_timing = ['*']
        time_filter_func = pycallgraph.GlobbingFilter(
            include=self.config.include_timing,
            exclude=self.config.exclude_timing,
            fraction=float(self.config.time_fraction_threshhold),
            )

    def run(self):
        if not self.config.quiet:
            print(
                'Running trace with Python Call Graph v%s' %
                pycallgraph.__version__
            )

        return pycallgraph.PyCallGraph(config=self.config)
