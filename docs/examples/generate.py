#!/usr/bin/env python

import subprocess
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
    open('{}.rst'.format(info['name']), 'w').write(
        IMAGE_TEMPLATE.format(info)
    )

    subprocess.call('./{}.py'.format(info['name']))

    if 'execute_after' in info:
        print('Running {}'.format(info['execute_after']))
        subprocess.call(info['execute_after'], shell=True)

