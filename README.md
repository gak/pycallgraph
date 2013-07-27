# Python Call Graph

[![Build Status](https://travis-ci.org/gak/pycallgraph.png)](https://travis-ci.org/gak/pycallgraph)

pycallgraph is a Python module that creates call graphs for Python programs.

## Features

* Support for Python 2.7+, Python 3.0+
* Static and interactive visualisations of the call graph using various tools such as Graphviz, Gephi, Ubigraph.
* Modules can be grouped together visually
* Easily extendable to create your own output formats.

### TODO

* Real-time call graphs can be generated and interactively viewed while profiling into D3.js, Gephi, Ubigraph. (#105)

## Installation

pycallgraph can be installed via pip or easy_install:

    pip install pycallgraph

## Basic Usage

**Note**: Version 1.0.0 of pycallgraph broke backwards compatibility in the API and command-line.

pycallgraph can be used with either the command-line, or via the module.

### Command-Line

    pycallgraph graphviz -- ./mypythonscript.py

Assuming you have Graphviz installed and in your path, this will generate a graphviz file in the working directory called "pycallgraph.png".

For more information, see the [command-line usage](https://pycallgraph.readthedocs.org/) in the documentation.

### API Usage

The absolute basic usage via the API (for version 1.0.0+) is:

    from pycallgraph import PyCallGraph

    pycg = PyCallGraph()
    pycg.start()

    code_to_profile()

    pycg.done()

Similar to the command-line example above, this will create a "pycallgraph.png" in your working directory.

To create different types of output, read up on [different output types](https://pycallgraph.readthedocs.org/).
