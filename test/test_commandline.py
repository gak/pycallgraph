import subprocess

from helpers import *


def execute(arguments):
	return subprocess.check_output(
		'PYTHONPATH=. scripts/pycallgraph ' + arguments, shell=True)


def test_help():
	assert 'Python Call Graph' in execute('--help')

def test_graphviz_help():
	assert '--font-name FONT_NAME' in execute('graphviz --help')
