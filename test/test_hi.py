def test_empty(pycg):
    pycg.start()
    pycg.stop()

    print(pycg.tracer.call_dict)
    print(pycg.tracer.call_stack)
    print(pycg.tracer.func_count)

def test_output(pycg, dot):
    pycg.add_output(dot)
    pycg.start()
    pycg.done()

    assert dot.fp.getvalue() != ''

def test_font_size(config):
    config.font_size = 20
    output = pycallgraph.GraphvizOutput(config)
    pycg = pycallgraph.PyCallGraph(config)
    pycg.done()

'''
config = pycallgraph.Config()
config.font_size = 20

output = pycallgraph.GraphvizOutput(config)
pycg = pycallgraph.PyCallGraph(config)

'''
