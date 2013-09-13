import collections

from .output import Output
from .graphviz import GraphvizOutput
from .gephi import GephiOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput
from .json import JsonOutput


outputters = collections.OrderedDict([
    ('graphviz', GraphvizOutput),
    ('gephi', GephiOutput),
    ('ubigraph', UbigraphOutput),
    ('json', JsonOutput),
])
