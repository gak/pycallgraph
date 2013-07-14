import inspect
import sys
import math
import os
import re
import tempfile
import time
from distutils import sysconfig


from .globbing_filter import GlobbingFilter

#NOTE: Should we make sure this import trys to look locally?
#TODO: Load only when the memory profiler option is active
from .memory_profiler import memory_usage


class Tracer(object):

    def __init__(self, outputs, config):
        self.outputs = outputs
        self.config = config
        self.updatables = [a for a in self.outputs if a.should_update()]

        self.init_trace_data()
        self.init_libpath()

    def init_trace_data(self):
        self.previous_event_return = False

        # A mapping of which function called which other function
        self.call_dict = {}

        # Current call stack
        self.call_stack = ['__main__']

        # Counters for each function
        self.func_count = {}
        self.func_count_max = 0

        # Accumulative time per function
        self.func_time = {}
        self.func_time_max = 0

        # Accumulative memory addition per function
        self.func_memory_in = {}
        self.func_memory_in_max = 0

        # Accumulative memory addition per function once exited
        self.func_memory_out = {}
        self.func_memory_out_max = 0

        # Keeps track of the start time of each call on the stack
        self.call_stack_timer = []
        self.call_stack_memory_in = []
        self.call_stack_memory_out = []

        # Filters to determine which calls to keep
        self.trace_filter = GlobbingFilter(exclude=['pycallgraph.*'])
        self.time_filter = GlobbingFilter()
        self.mem_filter = GlobbingFilter()

    def init_libpath(self):
        self.lib_path = sysconfig.get_python_lib()
        path = os.path.split(self.lib_path)
        if path[1] == 'site-packages':
            self.lib_path = path[0]
        self.lib_path = self.lib_path.lower()

    def start(self):
        sys.settrace(self.tracer)

    def stop(self):
        sys.settrace(None)

    def tracer(self, frame, event, arg):
        '''This function is called every time a call is made during a trace. It
        keeps track of relationships between calls.
        '''
        # Deal with memory when function has finished so local variables can be cleaned up
        if self.previous_event_return:
            self.previous_event_return = False
            cur_mem = memory_usage(-1, 0)

            if self.call_stack_memory_out:
                full_name, m = self.call_stack_memory_out.pop(-1)
            else:
                full_name, m = (None, None)

            # NOTE: Call stack is no longer the call stack that may be expected. Potentially
            # need to store a copy of it.
            if full_name and m and self.mem_filter(stack=self.call_stack, full_name=full_name):
                call_memory = (cur_mem[0] - m)
                if full_name not in self.func_memory_out:
                    self.func_memory_out[full_name] = 0
                else:
                    self.func_memory_out[full_name] += call_memory
                if self.func_memory_out[full_name] > self.func_memory_out_max:
                    self.func_memory_out_max = self.func_memory_out[full_name]

        if event == 'call':
            keep = True
            code = frame.f_code

            # Stores all the parts of a human readable name of the current call.
            full_name_list = []

            # Work out the module name
            module = inspect.getmodule(code)
            if module:
                module_name = module.__name__
                module_path = module.__file__
                if not self.config.include_stdlib \
                    and self.is_module_stdlib(module_path):
                    keep = False
                if module_name == '__main__':
                    module_name = ''
            else:
                module_name = ''
            if module_name:
                full_name_list.append(module_name)

            # Work out the class name.
            try:
                class_name = frame.f_locals['self'].__class__.__name__
                full_name_list.append(class_name)
            except (KeyError, AttributeError):
                class_name = ''

            # Work out the current function or method
            func_name = code.co_name
            if func_name == '?':
                func_name = '__main__'
            full_name_list.append(func_name)

            # Create a readable representation of the current call
            full_name = '.'.join(full_name_list)

            # Load the trace filter, if any. 'keep' determines if we should ignore
            # this call
            if keep and self.trace_filter:
                keep = self.trace_filter(self.call_stack, module_name,
                    class_name, func_name, full_name)

            # Store the call information
            if keep:

                if self.call_stack:
                    fr = self.call_stack[-1]
                else:
                    fr = None
                if fr not in self.call_dict:
                    self.call_dict[fr] = {}
                if full_name not in self.call_dict[fr]:
                    self.call_dict[fr][full_name] = 0
                self.call_dict[fr][full_name] += 1

                if full_name not in self.func_count:
                    self.func_count[full_name] = 0
                self.func_count[full_name] += 1
                if self.func_count[full_name] > self.func_count_max:
                    self.func_count_max = self.func_count[full_name]

                self.call_stack.append(full_name)
                self.call_stack_timer.append(time.time())

                self.cur_mem = memory_usage(-1, 0)
                self.call_stack_memory_in.append(self.cur_mem[0])
                self.call_stack_memory_out.append([full_name, self.cur_mem[0]])

            else:
                self.call_stack.append('')
                self.call_stack_timer.append(None)

        if event == 'return':

            self.previous_event_return = True

            if self.call_stack:
                full_name = self.call_stack.pop(-1)

                if self.call_stack_timer:
                    t = self.call_stack_timer.pop(-1)
                else:
                    t = None

                if t and self.time_filter(stack=self.call_stack, full_name=full_name):
                    if full_name not in self.func_time:
                        self.func_time[full_name] = 0
                    call_time = (time.time() - t)
                    self.func_time[full_name] += call_time
                    if self.func_time[full_name] > self.func_time_max:
                        self.func_time_max = self.func_time[full_name]

                if self.call_stack_memory_in:
                    m = self.call_stack_memory_in.pop(-1)
                else:
                    m = None

                if m and self.mem_filter(stack=self.call_stack, full_name=full_name):
                    if full_name not in self.func_memory_in:
                        self.func_memory_in[full_name] = 0
                    cur_mem = memory_usage(-1, 0)
                    call_memory = (cur_mem[0] - m)
                    self.func_memory_in[full_name] += call_memory
                    if self.func_memory_in[full_name] > self.func_memory_in_max:
                        self.func_memory_in_max = self.func_memory_in[full_name]

        return self.tracer

    def is_module_stdlib(self, file_name):
        '''Returns True if the file_name is in the lib directory.'''
        return file_name.lower().startswith(self.lib_path)

    def frac_calculation(self, func, count):
        calls_frac = float(count) / self.func_count_max
        try:
            total_time = self.func_time[func]

        except KeyError:
            total_time = 0
        try:
            total_time_frac = float(total_time) / self.func_time_max
        except ZeroDivisionError:
            total_time_frac = 0

        try:
            total_memory_in = self.func_memory_in[func]
            total_memory_out = self.func_memory_out[func]

        except KeyError:
            total_memory_in = 0
            total_memory_out = 0
        try:
            total_memory_in_frac = float(total_memory_in) / self.func_memory_in_max
            total_memory_out_frac = float(total_memory_out) / self.func_memory_out_max
        except ZeroDivisionError:
            total_memory_in_frac = 0
            total_memory_out_frac = 0

        return calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, total_memory_out_frac, total_memory_out

    def __getstate__(self):
        odict = self.__dict__.copy()
        dont_keep = [
            'outputs',
            'config',
            'updatables',
            'lib_path',
        ]
        for key in dont_keep:
            del odict[key]

        return odict

def simple_memoize(callable_object):
    '''Simple memoization for functions without keyword arguments.

    This is useful for mapping code objects to module in this context.
    inspect.getmodule() requires a number of system calls, which may slow down
    the tracing considerably. Caching the mapping from code objects (there is
    *one* code object for each function, regardless of how many simultaneous
    activations records there are).

    In this context we can ignore keyword arguments, but a generic memoizer
    ought to take care of that as well.
    '''

    cache = dict()

    def wrapper(*rest):
        if rest not in cache:
            cache[rest] = callable_object(*rest)
        return cache[rest]

    return wrapper

inspect.getmodule = simple_memoize(inspect.getmodule)
