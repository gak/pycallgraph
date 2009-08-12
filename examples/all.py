#!/usr/bin/env python
from glob import glob
from os import path
import sys

ROOT = path.join(path.abspath(path.dirname(__file__)), '..')
sys.path.insert(0, ROOT)

import pycallgraph

examples = glob('*.py')
examples.remove('all.py')
for example in examples:
    pycallgraph.reset_settings()
    print(example)
    execfile(example)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
