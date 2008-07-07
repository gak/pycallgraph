#!/bin/bash
epydoc --html -v --graph=classtree --no-frames --url=http://pycallgraph.slowchop.com/ --name=pycallgraph -o doc ../pycallgraph.py
scp -r doc/* gakman.com:/var/www/slowchop.com/pycallgraph/doc/

