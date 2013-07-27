#!/usr/bin/env python

from os import path
from setuptools import setup

# TODO: Have the version in only one place
__version__ = '1.0.0'

# Only install the man page if the correct directory exists
# XXX: Commented because easy_install doesn't like it
#man_path = '/usr/share/man/man1/'
#if path.exists(man_path):
#    data_files=[['/usr/share/man/man1/', ['man/pycallgraph.1']]]
#else:
#    data_files=None

data_files=None

setup(
    name='pycallgraph',
    version=__version__,
    description='Python Call Graph uses GraphViz to generate call graphs ' \
        'from one execution of your Python code.',
    author='Gerald Kaszuba',
    author_email='pycallgraph@slowchop.com',
    url='http://pycallgraph.slowchop.com/',
    packages=['pycallgraph', 'pycallgraph.output'],
    scripts=['scripts/pycallgraph'],
    data_files=data_files,
    use_2to3=True,

    # TODO: Update download_url
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
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
    ],
)
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
