import collections

from .output import Output
from .graphviz import GraphvizOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput


outputters = collections.OrderedDict([
    ('graphviz', GraphvizOutput),
    ('ubigraph', UbigraphOutput),
])
