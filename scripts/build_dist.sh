rm -fr build dist
python setup.py sdist --formats=gztar,zip
python setup.py bdist_wininst

