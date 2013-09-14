#!/usr/bin/env python

import subprocess
import yaml


INDEX_TEMPLATE = '''
Examples
========

.. toctree::
   :maxdepth: 3

   {}
'''


IMAGE_TEMPLATE = '''
.. _{0[name]}_example:

{0[title]}
===================

{0[description]}

Source Code
-----------

.. literalinclude:: {0[script]}

Generated Image
---------------

Below is the generated image from the code above. If you're having issues with the image below, try the :download:`direct link to image <{0[name]}.png>`.

.. container:: example-image

    .. image:: {0[name]}.png
        :target: ../_downloads/{0[name]}.png

'''


index = []


for info in yaml.load(open('examples.yml')):
    open('{}.rst'.format(info['name']), 'w').write(
        IMAGE_TEMPLATE.format(info).strip()
    )

    print(info['run'])
    subprocess.call(info['run'], shell=True)

    if 'execute_after' in info:
        print('Running {}'.format(info['execute_after']))
        subprocess.call(info['execute_after'], shell=True)

    index.append(info['name'])


open('index.rst', 'w').write(INDEX_TEMPLATE.format('\n   '.join(index)))