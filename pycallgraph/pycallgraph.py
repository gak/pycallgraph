import locale
import warnings

from .output import Output
from .config import Config
from .tracer import AsyncronousTracer, SyncronousTracer
from .exceptions import PyCallGraphException


class PyCallGraph(object):

    def __init__(self, outputs=None, config=None):
        '''outputs can be a single Output instance or an iterable with many
        of them.  Some examples:

        >>> PyCallGraph(output=GraphvizOutput())

        >>> PyCallGraph(output=[D3Output(), GephiOutput()])
        '''
        locale.setlocale(locale.LC_ALL, '')

        if outputs is None:
            self.outputs = []
        elif isinstance(outputs, Output):
            self.outputs = [outputs]
        else:
            self.outputs = outputs

        self.config = config or Config()
        configured_ouput = self.config.get_output()
        if configured_ouput:
            self.outputs.append(configured_ouput)

        self.reset()

    def __enter__(self):
        self.start()

    def __exit__(self, type, value, traceback):
        self.done()

    def get_tracer_class(self):
        if self.config.threaded:
            return AsyncronousTracer
        else:
            return SyncronousTracer

    def reset(self):
        '''Resets all collected statistics.  This is run automatically by
        start(reset=True) and when the class is initialized.
        '''
        self.tracer = self.get_tracer_class()(self.outputs, config=self.config)

        for output in self.outputs:
            self.prepare_output(output)

    def start(self, reset=True, filter_func=None, time_filter_func=None,
              memory_filter_func=None):
        '''Begins a trace.  Setting reset to True will reset all previously
        recorded trace data.  filter_func needs to point to a callable
        function that accepts the parameters (call_stack, module_name,
        class_name, func_name, full_name). Every call will be passed into
        this function and it is up to the function to decide if it should be
        included or not.  Returning False means the call will be filtered out
        and not included in the call graph.
        '''
        if not self.outputs:
            raise PyCallGraphException(
                'No outputs declared. Please see the '
                'examples in the online documentation.'
            )

        if reset:
            self.reset()

        for output in self.outputs:
            output.start()

        self.tracer.start()

    def stop(self):
        '''Stops the currently running trace, if any.'''
        self.tracer.stop()

    def done(self):
        '''Stops the trace and tells the outputters to generate their
        output.
        '''
        self.stop()

        # If in threaded mode, wait for the processor thread to complete
        self.tracer.done()

        for output in self.outputs:
            output.done()

    def add_output(self, output):
        self.outputs.append(output)
        self.prepare_output(output)

    def prepare_output(self, output):
        output.sanity_check()
        output.set_processor(self.tracer.processor)
        output.reset()
