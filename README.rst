Python Call Graph
#################

Welcome! Python Call Graph is a `Python <http://www.python.org>`_ module that creates `call graph <http://en.wikipedia.org/wiki/Call_graph>`_ visualizations for Python applications.

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

.. image:: https://pycallgraph.readthedocs.org/en/develop/_images/basic_thumb.png
    :target: https://pycallgraph.readthedocs.org/en/develop/examples/basic.html
.. image:: https://pycallgraph.readthedocs.org/en/develop/_images/regexp_grouped_thumb.png
    :target: https://pycallgraph.readthedocs.org/en/develop/examples/regexp_grouped.html
.. image:: https://pycallgraph.readthedocs.org/en/develop/_images/regexp_ungrouped_thumb.png
    :target: https://pycallgraph.readthedocs.org/en/develop/examples/regexp_ungrouped.html

Project Status
==============

The latest version is **1.0.0** which is currently in heavy development, and is a backwards incompatbile from the previous release.

Features
========

* Support for Python 2.7+ and Python 3.3+.
* Static visualizations of the call graph using various tools such as Graphviz and Gephi.
* Modules can be visually grouped together.
* Easily extendable to create your own output formats.

Quick Start
===========

Installation is easy as::

    pip install pycallgraph

You can either use the `command-line interface <https://pycallgraph.readthedocs.org/en/develop/guide/command_line_usage.html>`_ for a quick visualization of your Python script, or the `pycallgraph module <https://pycallgraph.readthedocs.org/en/develop/api/pycallgraph.html>`_ for more fine-grained settings.

The following examples specify graphviz as the outputter, so it's required to be installed. They will generate a file called **pycallgraph.png**.

The command-line method of running pycallgraph is::

    $ pycallgraph graphviz -- ./mypythonscript.py

A simple use of the API is::

    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        code_to_profile()

Documentation
=============

Feel free to browse the `documentation of pycallgraph <https://pycallgraph.slowchop.com/en/latest/>`_ for the `usage guide <https://pycallgraph.slowchop.com/en/latest/guide/>`_ and `API reference <https://pycallgraph.slowchop.com/en/latest/api/>`_.
