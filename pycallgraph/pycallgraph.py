'''
pycallgraph - Python Call Graph

U{http://pycallgraph.slowchop.com/}

Copyright Gerald Kaszuba 2007-2013

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
'''

__version__ = '0.6.0'
__author__ = 'Gerald Kaszuba'

# TODO Add additional authors in __credis__ ?
# __credits__ = '??'

from .output import Output
from .config import Config
from .tracer import Tracer
from .exceptions import PyCallGraphException


class PyCallGraph(object):

    def __init__(self, outputs=None, config=None):
        '''outputs can be a single Output instance or an iterable with many
        of them.  For example:

        PyCallGraph(output=[D3Output(), GephiOutput()])
        '''
        if outputs is None:
            self.outputs = []
        elif isinstance(outputs, Output):
            self.outputs = [outputs]
        else:
            self.outputs = outputs

        self.config = config or Config()

        self.reset()

    def reset(self):
        '''Resets all collected statistics.  This is run automatically by
        start(reset=True) and when the class is initialized.
        '''
        self.tracer = Tracer(outputs=self.outputs, config=self.config)

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
        if reset:
            self.reset()

        self.tracer.start()

    def stop(self):
        '''Stops the currently running trace, if any.'''
        self.tracer.stop()

    def done(self):
        '''Stops the trace and tells the outputters to generate their output.'''
        self.stop()

        for output in self.outputs:
            output.done()

    def add_output(self, output):
        self.outputs.append(output)
        self.prepare_output(output)

    def prepare_output(self, output):
        output.sanity_check()
        output.set_tracer(self.tracer)
        output.reset()


#class GephiOutput(Output):
#    pass


#class AnsiOutput(Output):
#    pass


#class MatrixOutput(Output):
#    pass


#class D3Output(Output):
#    pass


#class UbigraphOutput(Output):
#    pass


def reset_settings():
    global settings
    global graph_attributes
    global __version__

    settings = {
        'dont_exclude_anything': False,
        'include_stdlib': True,
    }

def get_gdf(stop=True):
    """Returns a string containing a GDF file. Setting stop to True will cause
    the trace to stop.
    """
    ret = ['nodedef>name VARCHAR, label VARCHAR, hits INTEGER, ' + \
            'calls_frac DOUBLE, total_time_frac DOUBLE, ' + \
            'total_time DOUBLE, color VARCHAR, width DOUBLE, total_memory_in_frac DOUBLE, total_memory_in DOUBLE']
    for func, hits in func_count.items():
        calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, \
            total_memory_out_frac, total_memory_out == _frac_calculation(func, hits)
        col = settings['node_colour'](calls_frac, total_time_frac)
        color = ','.join([str(round(float(c) * 255)) for c in col.split()])
        if time_filter==None or time_filter.fraction < total_time_frac:
            ret.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,\'%s\',%s' % (func, func, hits, \
                    calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, total_memory_out, color, \
                    math.log(hits * 10)))

    ret.append('edgedef>node1 VARCHAR, node2 VARCHAR, color VARCHAR')
    for fr_key, fr_val in call_dict.items():
        if fr_key == '':
            continue
        for to_key, to_val in fr_val.items():
            calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, \
               total_memory_out_frac, total_memory_out =  _frac_calculation(to_key, to_val)
            col = settings['edge_colour'](calls_frac, total_time_frac)
            color = ','.join([str(round(float(c) * 255)) for c in col.split()])
            if time_filter==None or time_filter.fraction < total_time_frac:
                ret.append('%s,%s,\'%s\'' % (fr_key, to_key, color))
    ret = '\n'.join(ret)
    return ret


def save_dot(filename):
    """Generates a DOT file and writes it into filename."""
    open(filename, 'w').write(get_dot())


def save_gdf(filename):
    """Generates a GDF file and writes it into filename."""
    open(filename, 'w').write(get_gdf())


def make_graph(filename, format=None, tool=None, stop=None):
    """This has been changed to make_dot_graph."""
    raise PyCallGraphException( \
        'make_graph is depricated. Please use make_dot_graph')


def make_gdf_graph(filename, stop=True):
    """Create a graph in simple GDF format, suitable for feeding into Gephi,
    or some other graph manipulation and display tool. Setting stop to True
    will stop the current trace.
    """
    if stop:
        stop_trace()

    try:
        f = open(filename, 'w')
        f.write(get_gdf())
    finally:
        if f: f.close()

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
