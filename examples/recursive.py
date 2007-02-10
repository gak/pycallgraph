import pycallgraph

pycallgraph.start_trace()

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

for a in xrange(1, 10):
    print factorial(a)

pycallgraph.make_graph('recursive.png')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

