"""
pycallgraph
This script is the command line interface to the pycallgraph make_dot_graph
method.

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
import sys
from optparse import OptionParser

import pycallgraph

parser = OptionParser(usage='%prog [options] pythonfile imagefile')
parser.add_option('-f', '--image-format', dest='format', default='png',
    help='The image format of imagefile. Default: png')
parser.add_option('-t', '--tool', dest='tool', default='dot',
    help='The tool from graphviz to use. Default: dot')
(options, args) = parser.parse_args()

if len(args) < 2:
    parser.print_help()
    sys.exit(0)

pycallgraph.start_trace()
execfile(args[0], globals(), locals())
pycallgraph.make_dot_graph(args[1], options.format, options.tool)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
