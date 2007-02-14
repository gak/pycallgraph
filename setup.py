#!/usr/bin/env python

from distutils.core import setup

from pycallgraph import __version__

setup(
    name='pycallgraph',
    version=__version__,
    description='Python Call Graph',
    author='Gerald Kaszuba',
    author_email='pycallgraph@gakman.com',
    url='http://pycallgraph.slowchop.com/',
    py_modules=['pycallgraph'],
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

