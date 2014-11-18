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

*OUTPUT_MODE* can be one of graphviz or gephi. *python_file.py* is a python script that will be traced and afterwards, a call graph visualization will be generated.

General Arguments
-----------------

.. cmdoption:: <OUTPUT_MODE>

    A choice of graphviz or gephi.

.. cmdoption:: -h, --help

   Shows a list of possible options for the command line.

.. cmdoption:: -v, --verbose

   Turns on verbose mode which will print out information of pycallgraph's state and processing.

.. cmdoption:: -d, --debug

   Turns on debug mode which will print out debugging information such as the raw Graphviz generated files.

.. cmdoption:: -ng, --no-groups

   Do not group modules in the results. By default this is turned on and will visually group together methods of the same module. The technique of grouping does rely on the type of output used.

.. cmdoption:: -s, --stdlib

   When running a trace, also include the Python standard library.

.. cmdoption:: -m, --memory

   An experimental option which includes memory tracking in the trace.

.. cmdoption:: -t, --threaded

   An experimental option which processes the trace in another thread. This may or may not be faster.

Filtering Arguments
-------------------

.. cmdoption:: -i, --include <pattern>

  Wildcard pattern of modules to include in the output. You can have multiple include arguments.

.. cmdoption:: -e, --exclude <pattern>

  Wildcard pattern of modules to exclude in the output. You can have multiple include arguments.
  
.. cmdoption:: --include-pycallgraph

  By default pycallgraph filters itself out of the trace. Enabling this will include pycallgraph in the trace.

.. cmdoption:: --max-depth

  Maximum stack depth to trace. Any calls made past this stack depth are not included in the trace.


Graphviz Arguments
------------------

.. cmdoption:: -l <tool>, --tool <tool>

  Modify the default Graphviz tool used by pycallgraph. It uses "dot", but can be changed to either neato, fdp, sfdp, twopi, or circo.

Examples
--------

Create a call graph image called pycallgraph.png on myprogram.py::

    pycallgraph graphviz -- ./myprogram.py

Create a call graph of a standard Python installation script with command line parameters::

    pycallgraph graphviz --output-file=setup.png -- setup.py --dry-run install

Run Django's *manage.py* script, but since there are many calls within Django, and will cause a massively sized generated image, we can filter it to only trace the core Django modules::

    pycallgraph -v --stdlib --include "django.core.*" graphviz -- ./manage.py syncdb --noinput
