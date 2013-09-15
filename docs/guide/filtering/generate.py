#!/usr/bin/env python

import hashlib
import subprocess
import yaml


items = yaml.load(open('examples.yml'))

print(items)

changed = False

for script, save_md5 in items.iteritems():
    new_md5 = hashlib.md5(open(script).read()).hexdigest()
    if new_md5 == save_md5:
        continue
    changed = True
    items[script] = new_md5
    subprocess.call('./{}'.format(script), shell=True)

if changed:
    open('examples.yml', 'w').write(yaml.dump(items))
