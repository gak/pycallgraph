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

parser.add_option(
    '-f', '--image-format', dest='format', default='png',
    help='The image format of imagefile. Default: png',
    )

parser.add_option(
    '-t', '--tool', dest='tool', default='dot',
    help='The tool from graphviz to use. Default: dot',
    )

parser.add_option(
    '-i', '--include', dest='include', default=[],
    action='append',
    help='Wildcard pattern of modules to include in the output.',
    )

parser.add_option(
    '-e', '--exclude', dest='exclude', default=[],
    action='append',
    help='Wildcard pattern of modules to exclude in the output. ' \
        'You can have multiple exclude arguments.',
    )

parser.add_option(
    '-d', '--max-depth', dest='max_depth', default=None,
    help='Maximum stack depth to trace.',
    )

(options, args) = parser.parse_args()

if len(args) < 2:
    parser.print_help()
    sys.exit(0)

# Create globbing filter
if not options.include:
    options.include = ['*']
glob_filter = pycallgraph.GlobbingFilter(
    include=options.include,
    exclude=options.exclude,
    max_depth=options.max_depth,
    )

pycallgraph.start_trace(filter_func=glob_filter)
execfile(args[0], globals(), locals())
pycallgraph.make_dot_graph(args[1], options.format, options.tool)

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
