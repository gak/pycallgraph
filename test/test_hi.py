import pickle


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

def test_pickle(pycg, pickle_output):
    pycg.add_output(pickle_output)
    pycg.start()
    import re
    re.compile('asdf.*asdf[1ab]+34$')
    pycg.done()

    tracer = pickle.loads(pickle_output.fp.getvalue())

    print(tracer)
    print(tracer.__dict__)
