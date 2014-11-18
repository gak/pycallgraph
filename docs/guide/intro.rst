Intro
=====

Python Call Graph was made to be a visual profiling tool for Python applications. It uses a debugging Python function called `sys.set_trace() <http://docs.python.org/dev/library/sys#sys.settrace>`_ which makes a callback every time your code enters or leaves function. This allows Python Call Graph to track the name of every function called, as well as which function called which, the time taken within each function, number of calls, etc.

It is able to generate different types of :ref:`outputs and visualizations <outputs>`. Initially Python Call Graph was only used to generate DOT files for `GraphViz <http://graphviz.org/>`_, and as of version 1.0.0, it can also generate GDF files for Gephi. Creating :ref:`custom outputs <custom_outputs>` is fairly easy by subclassing the :ref:`Output <output>` class.

You can either use the :ref:`command-line interface <command_line_usage>` for a quick visualization of your Python script, or the :ref:`pycallgraph module <pycallgraph>` for more fine-grained settings.

.. todo:: Add some examples and screenshots
