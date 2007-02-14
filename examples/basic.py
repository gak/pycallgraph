import pycallgraph

pycallgraph.start_trace()

class Banana:
    def __init__(self):
        pass
    def eat(self):
        pass

banana = Banana()
banana.eat()

pycallgraph.make_dot_graph('basic.png')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

