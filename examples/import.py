import pycallgraph

import_list = ['pickle', 'ctypes', 'htmllib']

for imp in import_list:
    pycallgraph.start_trace()
    __import__(imp)
    pycallgraph.make_graph('import-%s.png' % imp)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

