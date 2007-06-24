"""
pycallgraph

U{http://pycallgraph.slowchop.com/}

Copyright Gerald Kaszuba 2007

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import inspect
import sys
import os
import re
import tempfile
import time

# Initialise module variables
trace_filter = None

call_dict = {}

# current call stack
call_stack = ['__main__']

# counters for each function
func_count = {}
func_count_max = 0

# accumative time per function
func_time = {}
func_time_max = 0

# keeps track of the start time of each call on the stack
call_stack_timer = []

# graphviz settings
graph_attributes = {
    'graph': {
    },
    'node': {
        'color': '.5 0 .9',
        'style': 'filled',
        'shape': 'rect',
        'fontname': 'Helvetica',
        'fontsize': 10,
    },
}

# settings for building dot files
def colourize_node(calls, total_time):
    value = float(total_time * 2 + calls) / 3
    return '%f %f %f' % (value / 2 + .5, value, 0.9)

def colourize_edge(calls, total_time):
    value = float(total_time * 2 + calls) / 3
    return '%f %f %f' % (value / 2 + .5, value, 0.7)

settings = {
    'node_attributes': {
       'label': r'%(func)s\ncalls: %(hits)i\ntotal time: %(total_time)f',
       'color': '%(col)s',
    },
    'node_colour': colourize_node,
    'edge_colour': colourize_edge,
    'dont_exclude_anything': False,
}


def reset_trace():
    """Resets all collected statistics. This is run automatically by
    start_trace(reset=True) and when the module is loaded.
    """
    global call_dict
    global call_stack
    global func_count
    global func_count_max

    call_dict = {}
    call_stack = ['__main__']
    func_count = {}
    func_count_max = 0


class PyCallGraphException(Exception):
    """Exception used for pycallgraph"""
    pass


class GlobbingFilter(object):
    """Filter module names using a set of globs.

    Objects are matched against the exclude list first, then the include list.
    Anything that passes through without matching either, is excluded.
    """

    def __init__(self, include=None, exclude=None, max_depth=None):
        if include is None and exclude is None:
            include = ['*']
            exclude = []
        elif include is None:
            include = ['*']
        elif exclude is None:
            exclude = []
        self.include = include
        self.exclude = exclude
        self.max_depth = max_depth or 9999

    def __call__(self, stack, module_name, class_name, func_name, \
                 full_name):
        from fnmatch import fnmatch
        if len(stack) > self.max_depth:
            return False
        for pattern in self.exclude:
            if fnmatch(full_name, pattern):
                return False
        for pattern in self.include:
            if fnmatch(full_name, pattern):
                return True
        return False


def start_trace(reset=True, filter_func=None):
    """Begins a trace. Setting reset to True will reset all previously recorded
    trace data. filter_func needs to point to a callable function that accepts
    the parameters (call_stack, module_name, class_name, func_name, full_name).
    Every call will be passed into this function and it is up to the function
    to decide if it should be included or not. Returning False means the call
    will be filtered out and not included in the call graph.
    """
    global trace_filter
    if reset:
        reset_trace()
    if filter_func is None:
        trace_filter = GlobbingFilter(exclude=['pycallgraph.*'])
    else:
        trace_filter = filter_func
    sys.settrace(tracer)


def stop_trace():
    """Stops the currently running trace, if any."""
    sys.settrace(None)


def tracer(frame, event, arg):
    """This is an internal function that is called every time a call is made
    during a trace. It keeps track of relationships between calls.
    """
    global func_count_max
    global func_count
    global trace_filter
    global call_stack
    global func_time
    global func_time_max

    if event == 'call':
        keep = True
        code = frame.f_code

        # Stores all the parts of a human readable name of the current call.
        full_name_list = []

        # Work out the module name
        module = inspect.getmodule(code)
        if module:
            module_name = module.__name__
            if module_name == '__main__':
                module_name = ''
        else:
            module_name = 'unknown'
            keep = False
        full_name_list.append(module_name)

        # Work out the class name.
        try:
            class_name = frame.f_locals['self'].__class__.__name__
        except (KeyError, AttributeError):
            class_name = ''
        if class_name:
            full_name_list.append(class_name)

        # Work out the current function or method
        func_name = code.co_name
        if func_name == '?':
            func_name = '__main__'
        full_name_list.append(func_name)

        # Create a readable representation of the current call
        full_name = '.'.join(full_name_list)

        # Load the trace filter, if any. 'keep' determines if we should ignore
        # this call
        if trace_filter:
            keep = trace_filter(call_stack, module_name, class_name,
                func_name, full_name)

        # Store the call information
        fr = call_stack[-1]
        if keep or settings['dont_exclude_anything']:

            if fr not in call_dict:
                call_dict[fr] = {}
            if full_name not in call_dict[fr]:
                call_dict[fr][full_name] = 0
            call_dict[fr][full_name] += 1

            if full_name not in func_count:
                func_count[full_name] = 0
            func_count[full_name] += 1
            if func_count[full_name] > func_count_max:
                func_count_max = func_count[full_name]

            call_stack.append(full_name)
            call_stack_timer.append(time.time())

        else:
            call_stack.append('')
            call_stack_timer.append(None)

    if event == 'return':
        if call_stack:
            full_name = call_stack.pop(-1)
            t = call_stack_timer.pop(-1)
            if t:
                if full_name not in func_time:
                    func_time[full_name] = 0
                call_time = (time.time() - t)
                func_time[full_name] += call_time
                if func_time[full_name] > func_time_max:
                    func_time_max = func_time[full_name]

    return tracer


def get_dot(stop=True):
    """Returns a string containing a DOT file. Setting stop to True will cause
    the trace to stop.
    """
    global func_time_max

    def frac_calculation(func, count):
        global func_count_max
        global func_time
        global func_time_max
        calls_frac = float(count) / func_count_max
        try:
            total_time = func_time[func]
        except KeyError:
            total_time = 0
        if func_time_max:
            total_time_frac = float(total_time) / func_time_max
        else:
            total_time_frac = 0
        return calls_frac, total_time_frac, total_time

    if stop:
        stop_trace()
    ret = ['digraph G {', ]
    for comp, comp_attr in graph_attributes.items():
        ret.append('%s [' % comp)
        for attr, val in comp_attr.items():
            ret.append('%(attr)s = "%(val)s",' % locals())
        ret.append('];')
    for func, hits in func_count.items():
        calls_frac, total_time_frac, total_time = frac_calculation(func, hits)
        col = settings['node_colour'](calls_frac, total_time_frac)
        attribs = ['%s="%s"' % a for a in settings['node_attributes'].items()]
        node_str = '"%s" [%s];' % (func, ','.join(attribs))
        ret.append(node_str % locals())
    for fr_key, fr_val in call_dict.items():
        if fr_key == '':
            continue
        for to_key, to_val in fr_val.items():
            calls_frac, total_time_frac, totla_time = \
                frac_calculation(to_key, to_val)
            col = settings['edge_colour'](calls_frac, total_time_frac)
            edge = '[ color = "%s" ]' % col
            ret.append('"%s"->"%s" %s' % (fr_key, to_key, edge))
    ret.append('}')
    return '\n'.join(ret)


def save_dot(filename):
    """Generates a DOT file and writes it into filename."""
    open(filename, 'w').write(get_dot())


def make_graph(filename, format=None, tool=None, stop=None):
    """This has been changed to make_dot_graph."""
    raise PyCallGraphException( \
        'make_graph is depricated. Please use make_dot_graph')


def make_dot_graph(filename, format='png', tool='dot', stop=True):
    """Creates a graph using a Graphviz tool that supports the dot language. It
    will output into a file specified by filename with the format specified.
    Setting stop to True will stop the current trace.
    """
    if stop:
        stop_trace()

    # create a temporary file to be used for the dot data
    fd, tempname = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write(get_dot())
    f.close()

    # normalize filename
    regex_user_expand = re.compile('\A~')
    if regex_user_expand.match(filename):
        filename = os.path.expanduser(filename)
    else:
        filename = os.path.expandvars(filename)  # expand, just in case

    cmd = '%(tool)s -T%(format)s -o%(filename)s %(tempname)s' % locals()
    try:
        ret = os.system(cmd)
        if ret:
            raise PyCallGraphException( \
                'The command "%(cmd)s" failed with error ' \
                'code %(ret)i.' % locals())
    finally:
        os.unlink(tempname)

reset_trace()

__version__ = '0.4.0'
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
