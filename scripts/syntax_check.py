#!/usr/bin/env python

from os import path
ROOT = path.abspath(path.dirname(__file__))

import os
from glob import glob

os.chdir(os.path.join(ROOT, '..'))

for file in glob('*.py') + glob('examples/*py') + glob('scripts/*py'):
    os.system('scripts/pep8.py --repeat %s' % file)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
