Filtering
=========

Banana
------

Filtering is sometimes needed when the output of Python Call Graph is overwhelming, or if you want to only measure a small portion of your program. The filtering guide below is based on the `filter.py <https://github.com/gak/pycallgraph/blob/master/examples/filter.py>`_ example.

Let's demonstrate with a class that can eat a banana:

.. literalinclude:: filtering/banana.py

No Filter
---------

The code to measure it without any configuration, apart from the output file:

.. literalinclude:: filtering/filter_none.py

The Graphviz output after running the measurement code:

.. container:: example-image

    .. image:: filtering/filter_none.png

Hide the secret
---------------

Probably need to hide that **secret_function**. Create a :ref:`GlobbingFilter <globbing_filter>` which excludes **secret_function** along with **pycallgraph** so we don't see the internals. Add that filter to the config option called **trace_filter**:

.. literalinclude:: filtering/filter_exclude.py

And the output:

.. container:: example-image

    .. image:: filtering/filter_exclude.png

You can also use "include" as well as "exclude" in the :ref:`GlobbingFilter <globbing_filter>`.

Maximum Depth
-------------

Let's say you're only interested in the first level of calls. You can specify this using **config.max_depth**:

.. literalinclude:: filtering/filter_max_depth.py

And the output:

.. container:: example-image

    .. image:: filtering/filter_max_depth.png
