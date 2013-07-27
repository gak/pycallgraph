from helpers import *


def test_no_args(recwarn):
	pycg = PyCallGraph()
	pycg.start()
	pycg.done()
	recwarn.pop(RuntimeWarning)
