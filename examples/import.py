#!/usr/bin/env python
'''
This example shows the interals of certain Python modules when they are being
imported.
'''
import pycallgraph


def main():
    import_list = ['pickle', 'htmllib']

    for imp in import_list:
        pycallgraph.start_trace()
        __import__(imp)
        pycallgraph.make_dot_graph('import-%s.png' % imp)

if __name__ == '__main__':
    main()
