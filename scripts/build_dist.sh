#!/bin/bash
cd ..
rm -fr build dist
python setup.py clean
python setup.py sdist --formats=gztar,zip
python setup.py bdist_wininst
cd dist
scp * gakman.com:/var/www/slowchop.com/pycallgraph/download/

