import subprocess

from helpers import *


def execute(arguments):
    command = 'PYTHONPATH=. scripts/pycallgraph ' + arguments
    return subprocess.check_output(command, shell=True).decode('utf-8')


def test_help():
    assert 'Python Call Graph' in execute('--help')


def test_graphviz_help():
    assert '--font-name FONT_NAME' in execute('graphviz --help')
