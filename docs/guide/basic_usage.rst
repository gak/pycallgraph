Basic Usage
===========

**Note**: Version 1.0.0 of pycallgraph broke backwards compatibility in the API and command-line.

pycallgraph can be used with either the command-line, or via the module.

.. _command_line_tutorial:

Command-line Interface Tutorial
===============================

From the command line, execute:

.. code:: bash

	$ pycallgraph graphviz -- ./mypythonscript.py

Assuming you have Graphviz installed and in your path, and a **mypythonscript.py** script in the current directory, this will generate a graphviz file in the working directory called **pycallgraph.png**.

For more information, see the [command-line usage](https://pycallgraph.readthedocs.org/) in the documentation.

.. _api_tutorial:

API Tutorial
============

The absolute basic usage via the API (for version 1.0.0+) is:

.. code:: python

	from pycallgraph import PyCallGraph
	from pycallgraph.output import GraphvizImageOutput

	pycg = PyCallGraph(outputs=GraphvizImageOutput)
	pycg.start()

	code_to_profile()

	pycg.done()

Similar to the command-line example above, this will create a **pycallgraph.png** in your working directory.

To create different types of output, read up on [different output types](https://pycallgraph.readthedocs.org/).

