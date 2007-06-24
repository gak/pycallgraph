import os
from glob import glob

for file in glob('*.py') + glob('examples/*py') + glob('scripts/*py'):
    os.system('pep8.py --repeat %s' % file)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
