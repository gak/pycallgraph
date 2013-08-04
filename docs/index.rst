Python Call Graph
#################

Python Call Graph is a `Python <http://www.python.org>`_ module that creates `call graph <http://en.wikipedia.org/wiki/Call_graph>`_ visualisations for Python applications.

.. image:: https://travis-ci.org/gak/pycallgraph.png
    :target: https://travis-ci.org/gak/pycallgraph
.. image:: https://coveralls.io/repos/gak/pycallgraph/badge.png?branch=develop
    :target: https://coveralls.io/r/gak/pycallgraph?branch=develop
.. image:: https://pypip.in/v/pycallgraph/badge.png
    :target: https://crate.io/packages/pycallgraph/
.. image:: https://pypip.in/d/pycallgraph/badge.png
    :target: https://crate.io/packages/pycallgraph/

Screenshots
===========

Click on the images below to see a larger version and the source code that generated them.

Features
========

* Support for Python 2.7+, Python 3.0+
* Static and interactive visualisations of the call graph using various tools such as Graphviz, Gephi, Ubigraph.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.
* (The beginnings of) automated unit testing and a goal for 100% code coverage.

Quick Start
===========

Welcome to the Python Call Graph (pycallgraph) documentation. The latest version is **1.0.0** and is a backwards incompatbile from the previous release.

Installation is easy as::

    pip install pycallgraph

You can either use the :ref:`command-line interface <command_line_usage>` for a quick visualisation of your Python script, or the :ref:`pycallgraph module <pycallgraph>` for more fine-grained settings.

The following examples specify graphviz as the outputter, so it's required to be installed. They will generate a file called **pycallgraph.png**.

The command-line method of running pycallgraph is::

    $ pycallgraph graphviz -- ./mypythonscript.py

A simple use of the API is::

    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizImageOutput

    with PyCallGraph(outputs=GraphvizImageOutput):
        code_to_profile()


Documentation Index
===================

.. toctree::
    :maxdepth: 3

    guide/index
    api/api
    api/internal
