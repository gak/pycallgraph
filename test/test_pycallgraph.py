from helpers import *


def test_no_args(recwarn):
	pycg = PyCallGraph()
	pycg.start()
	pycg.done()
	recwarn.pop(RuntimeWarning)

def test_no_args(recwarn):
	with PyCallGraph():
		pass
	recwarn.pop(RuntimeWarning)
