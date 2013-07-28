# Python Call Graph

[![Build Status](https://travis-ci.org/gak/pycallgraph.png)](https://travis-ci.org/gak/pycallgraph) [![Coverage Status](https://coveralls.io/repos/gak/pycallgraph/badge.png?branch=develop)](https://coveralls.io/r/gak/pycallgraph?branch=develop) [![Version](https://pypip.in/v/pycallgraph/badge.png)](https://crate.io/packages/pycallgraph/) [![Downloads](https://pypip.in/d/pycallgraph/badge.png)](https://crate.io/packages/pycallgraph/)

pycallgraph is a Python module that creates call graphs for Python programs.

## Features

* Support for Python 2.7+, Python 3.0+
* Static and interactive visualisations of the call graph using various tools such as Graphviz, Gephi, Ubigraph.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.
* (The beginnings of) automated unit testing and a goal for 100% code coverage.

**Upcoming**

* Real-time call graphs can be generated and interactively viewed while profiling into D3.js, Gephi, Ubigraph. (#105)

## Installation

pycallgraph can be installed via pip or easy_install:

    pip install pycallgraph

## Documentation

The [documentation](https://pycallgraph.readthedocs.org/) has many [screenshots](), a quick start guide with [basic usage](https://pycallgraph.readthedocs.org/), a guide to [create your own output classes](https://pycallgraph.readthedocs.org/), and the [API reference](https://pycallgraph.readthedocs.org/).
