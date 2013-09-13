Intro
=====

Python Call Graph was made a visual profiling too for Python applications. It uses a debugging Python function called `sys.set_trace() <http://docs.python.org/dev/library/sys#sys.settrace>`_ which makes a callback every time your code enters or leaves function. This allows Python Call Graph to track the name of every function called, as well as which function called which, the time taken within each function, number of calls, etc.

It is able to generate different types of :ref:`outputs and visualizations <outputs>`. Initially Python Call Graph was only used to generate DOT files for GraphViz, and as of version 1.0, it can also generate JSON, Python pickles, and GDF for Gephi. Creating :ref:`custom outputs <custom_outputs>` is fairly easy by subclassing the :ref:`Output <output>` class.

It can be used in two different ways: the command-line interface and the pycallgraph module.

