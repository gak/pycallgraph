def test_empty(pycg):
    pycg.start()
    pycg.stop()

    print(pycg.tracer.call_dict)
    print(pycg.tracer.call_stack)
    print(pycg.tracer.func_count)

def test_graphviz_source(pycg, graphviz_source):
    pycg.add_output(graphviz_source)
    pycg.done()
    print(graphviz_source.fp.getvalue())

def test_graphviz_image(pycg, graphviz_image):
    pycg.add_output(graphviz_image)
    pycg.start()
    import re
    re.compile('asdf.*asdf[1ab]+34$')
    pycg.done()

'''
config = pycallgraph.Config()
output = pycallgraph.GraphvizOutput(config)
pycg = pycallgraph.PyCallGraph(config)


g = GraphvizOutput()
g.font_size = 5

p = PyCallGraph(output=g)

---- OR -----

./pycallgraph --include-stdlib graphviz-image --font-size 5 -o test.png

config = Config()
config.parse_args(sys.argv)

p = PyCallGraph(config=config)

'''
