rm -fr build dist
python setup.py clean
python setup.py sdist --formats=gztar,zip
python setup.py bdist_wininst
cd dist
scp * gakman.com:/home/httpd/html/slowchop.com/pycallgraph/download/
ssh gakman.com chgrp httpd /home/httpd/html/slowchop.com/pycallgraph/download/*
ssh gakman.com chmod a-wx,a+r /home/httpd/html/slowchop.com/pycallgraph/download/*

