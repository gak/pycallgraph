.. _command_line_usage:

Command-line Usage
==================

Synopsis
--------

pycallgraph [*OPTION*]... *OUTPUT_MODE* [*OUTPUT_OPTIONS*] *python_file.py*

Description
-----------

.. only:: man

	pycallgraph is a program that creates call graph visualization from Python scripts.

*OUTPUT_MODE* can be one of graphviz, gephi and ubigraph. *python_file.py* is a python script that will be traced and afterwards, a call graph visualization will be generated.

Arguments
---------

.. cmdoption:: -m <module>, --module <module>

   Run a module as a script.

.. cmdoption:: -m <module>, --module <module>

   Run a module as a script.

Examples
--------

Create a call graph image called pycallgraph.png on myprogram.py::

    pycallgraph graphviz ./myprogram.py

Create a call graph of a standard Python installation script with command line parameters::

    pycallgraph graphviz --output-file=setup.png -- setup.py --dry-run install

Only see the module "distutils" within the execution of easy_install::

    pycallgraph --include=distutils.* graphviz /usr/bin/easy_install
