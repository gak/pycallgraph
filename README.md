# Python Call Graph

[![Build Status](https://travis-ci.org/gak/pycallgraph.png)](https://travis-ci.org/gak/pycallgraph)

pycallgraph is a Python module that creates call graphs for Python programs.

## Features

* Support for Python 2.7+, Python 3.0+
* Generates static and interactive visualisations of the call graph using various tools such as Graphviz, Gephi, Ubigraph.
* pycallgraph's code is easily extendable to create your own output formats.

## Installation

pycallgraph can be installed via pip or easy_install:

    pip install pycallgraph

or

	easy_install pycallgraph

## Basic Usage

*Note*: Version 1.0.0 of pycallgraph broke backwards compatibility in the API and command-line.

pycallgraph can be used with either the command-line, or via the module.

### Command-Line

    pycallgraph graphviz -- ./mypythonscript.py

This will generate a graphviz file in the working directory called "pycallgraph.png".

## API Usage

The absolute basic usage via the API is:

    from pycallgraph import PyCallGraph

    pycg = PyCallGraph()
    pycg.start()

    code_to_profile()

    pycg.done()

This will generate a graphviz file in the working directory called "pycallgraph.png".

