import inspect
import sys

call_dict = {}
call_stack = ['__main__']

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

def write_dot(self, filename):
    f = open('yo.dot', 'w')
    f.write('digraph G {\n')
    for fr_key, fr_val in call_dict.items():
        for to_key, to_val in fr_val.items():
            r = float(to_val) / 50
            if r > 255:
                r = 255
            f.write('"%s"->"%s" [color = "#%02x0000"]\n' % (fr_key, to_key, r))
    f.write('}\n')

if __name__ == '__main__':

    def hello():
        pass

    start_trace()
    hello()
    stop_trace()

