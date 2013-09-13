#!/usr/bin/env python

import yaml

IMAGE_TEMPLATE = '''
.. _{0[name]}_example:

{0[title]}
===================

{0[description]}

.. literalinclude:: {0[name]}.py

:download:`Direct link to image <{0[name]}.png>`

.. container:: example-image

    .. image:: {0[name]}.png

'''

for info in yaml.load(open('examples.yml')):
    open('{}.rst'.format(info['name']), 'w')
    IMAGE_TEMPLATE.format(info))

