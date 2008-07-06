#!/bin/bash
rm -fr build dist
python setup.py clean
python setup.py sdist --formats=gztar,zip
python setup.py bdist_wininst
cd dist
scp * gakman.com:/var/html/slowchop.com/pycallgraph/download/

