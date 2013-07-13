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

'''
pycg = PyCallGraph()
'''
