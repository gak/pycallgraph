#!/usr/bin/env python
"""
pycallgraph

U{http://pycallgraph.slowchop.com/}

Copyright Gerald Kaszuba 2007

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

"""
This example shows the interals of certain Python modules when they are being
imported.
"""
import pycallgraph

pycallgraph.settings['dont_exclude_anything'] = True

import_list = ['pickle', 'htmllib']

for imp in import_list:
    pycallgraph.start_trace()
    __import__(imp)
    pycallgraph.make_dot_graph('import-%s.png' % imp)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
