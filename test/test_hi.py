def test_empty(pycg):
    pycg.start()
    pycg.stop()

    print(pycg.tracer.call_dict)
    print(pycg.tracer.call_stack)
    print(pycg.tracer.func_count)

def test_font_size(config):
    import fix_path
    import pycallgraph

    output = pycallgraph.output.GraphvizSourceOutput()

    from StringIO import StringIO
    output.fp = StringIO()
    config.font_size = 20

    pycg = pycallgraph.PyCallGraph(outputs=output)
    pycg.done()

    print(output.fp.getvalue())
    print("ASDfasdf")

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
