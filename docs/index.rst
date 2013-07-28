Python Call Graph
#################

Python Call Graph is a `Python <http://www.python.org>`_ module that creates `call graph <http://en.wikipedia.org/wiki/Call_graph>`_ visualisations for Python applications.

.. image:: https://travis-ci.org/gak/pycallgraph.png
	:target: https://travis-ci.org/gak/pycallgraph)
.. image:: https://coveralls.io/repos/gak/pycallgraph/badge.png?branch=develop
	:target: https://coveralls.io/r/gak/pycallgraph?branch=develop)
.. image:: https://pypip.in/v/pycallgraph/badge.png
	:target: https://crate.io/packages/pycallgraph/)
.. image:: https://pypip.in/d/pycallgraph/badge.png
	:target: https://crate.io/packages/pycallgraph/)

Screenshots
===========

Click on the images below to see a larger version and the source code that generated them.

Quick Start
===========

Welcome to the Python Call Graph (pycallgraph) documentation. The latest version is *1.0.0*.

You can either use the :ref:`command-line interface <command_line_tutorial>` for a quick visualisation of your Python script, or the :ref:`pycallgraph module <api_tutorial>` for more fine-grained settings.

Installation is easy as:

    pip install pycallgraph

**Note**: Version 1.0.0 of pycallgraph broke backwards compatibility in both the API and command-line.

Features
========

* Support for Python 2.7+, Python 3.0+
* Static and interactive visualisations of the call graph using various tools such as Graphviz, Gephi, Ubigraph.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.
* (The beginnings of) automated unit testing and a goal for 100% code coverage.

Documentation Index
===================

.. toctree::
	:maxdepth: 3

	guide/index
	api/api
	api/internal

