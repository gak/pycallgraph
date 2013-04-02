import gc
import numpy as np
from memory_profiler import memory_usage
import sys
global just_returned

def trace_calls_and_returns(frame, event, arg):
    
    global just_returned
    co = frame.f_code
    func_name = co.co_name

    if just_returned:
        just_returned = False
        print 'just_returned'
        print 'mem before gc ' + str(memory_usage(-1))
     #   gc.collect()
        print 'mem after gc ' + str(memory_usage(-1))
    
    if func_name == 'memory_usage':
        return
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print 'Call to %s on line %s of %s' % (func_name, line_no, filename)
        return trace_calls_and_returns
    elif event == 'return':
        print 'return of %s => %s' % (func_name, arg)
        just_returned = True
        print 'mem before gc ' + str(memory_usage(-1))
       # gc.collect()
        print 'mem after gc ' + str(memory_usage(-1))
    elif event == 'line':
        print 'a line event ' + str(line_no)
    return

def main():

    def take_memory():
    #   print memory_usage(-1)
        mem = np.zeros(100000)
        mem2 = np.zeros(1e8)
    #   print memory_usage(-1)
        return mem
    

    #print memory_usage(-1)
    take_memory()
    b = take_memory()
    gc.collect()
    a=b
    a=b=take_memory()
    b=a
    #print memory_usage(-1)
    #gc.collect()
    #print memory_usage(-1)
just_returned = False
#sys.settrace(trace_calls_and_returns)
main()
