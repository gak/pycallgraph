#!/usr/bin/env python

from os import path
from distutils.core import setup

from pycallgraph import __version__

# Only install the man page if the correct directory exists
# XXX: Commented because easy_install doesn't like it
#man_path = '/usr/share/man/man1/'
#if path.exists(man_path):
#    data_files=[['/usr/share/man/man1/', ['man/pycg.1']]]
#else:
#    data_files=None

data_files=None

setup(
    name='pycallgraph',
    version=__version__,
    description='Python Call Graph uses GraphViz to generate call graphs ' \
        'from one execution of your Python code.',
    author='Gerald Kaszuba',
    author_email='pycg@slowchop.com',
    url='http://pycallgraph.slowchop.com/',
    py_modules=['pycallgraph'],
    scripts=['scripts/pycg'],
    data_files=data_files,
    long_description = \
'''Python Call Graph uses GraphViz to generate call graphs from one execution
of your Python code. It's very easy to use and can point out possible problems
with your code execution.''',
    download_url =
    'http://pycallgraph.slowchop.com/files/download/pycallgraph-%s.tar.gz' % \
        __version__,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
        ],
)
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
