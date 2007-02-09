#!/usr/bin/env python
"""
pycallgraph
http://pycallgraph.slowchop.com/
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
import tempfile

call_dict = {}
call_stack = ['__main__']

class PyCallGraphException(Exception):
    pass

def start_trace():
    sys.settrace(tracer)

def stop_trace():
    sys.settrace(None)

def tracer(frame, event, arg):
    if event == 'call':
        dont_keep = False
        code = frame.f_code
   
        # work out the module
        module = inspect.getmodule(code)
        if module:
            module_name = module.__name__ + '.'
            if module_name == '__main__.':
                module_name = ''
        else:
            module_name = 'unknown.'
            dont_keep = True

        # work out the instance, if we're in a class
        try:
            class_name = frame.f_locals['self'].__class__.__name__ + '.'
        except (KeyError, AttributeError):
            class_name = ''

        # work out the current function or method
        func_name = code.co_name
        if func_name == '?':
            func_name = 'nofunc'
            dont_keep = True
        
        # join em together in a readable form
        full_name = '%s%s%s' % (module_name, class_name, func_name)

        # throw it all in a dict
        fr = call_stack[-1]
        to = full_name
        if not dont_keep:
            if fr not in call_dict:
                call_dict[fr] = {}
            if to not in call_dict[fr]:
                call_dict[fr][to] = 0
            call_dict[fr][to] += 1

        call_stack.append(to)
        return tracer
    if event == 'return':
        if call_stack:
            call_stack.pop(-1)

def get_dot():
    ret = ['digraph G {',]
    for fr_key, fr_val in call_dict.items():
        for to_key, to_val in fr_val.items():
            ret.append('"%s"->"%s"' % (fr_key, to_key))
    ret.append('}')
    return '\n'.join(ret)

def save_dot(filename):
    open(filename, 'w').write(get_dot())

def make_graph(filename, format='png', tool='dot'):
    fd, tempname = tempfile.mkstemp()
    f = os.fdopen(fd, 'w')
    f.write(get_dot())
    f.close()
    cmd = '%(tool)s -T%(format)s -o%(filename)s %(tempname)s' % locals()
    ret = os.system(cmd)
    os.unlink(tempname)
    if ret:
        raise PyCallGraphException('The command "%(cmd)s" failed with error' \
            'code %(ret)i.' % locals())

if __name__ == '__main__':
    
    class Yo:
        def hello(self):
            pass

    f = 'test.png'
    print 'Starting trace'
    start_trace()
    Yo().hello()
    stop_trace()
    print 'Generating graph'
    make_graph(f)
    print '%s should be in this directiory. Hit enter to quit.' % f
    raw_input()

__version__ = "$Revision: 53 $"
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

