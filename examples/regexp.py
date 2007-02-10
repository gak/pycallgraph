import pycallgraph
import re

pycallgraph.start_trace()

re.search('(hel[j-s]o).*(th[^e]*ere)', 'hello there')

pycallgraph.make_graph('regexp.png')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:

