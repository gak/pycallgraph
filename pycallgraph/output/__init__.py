from .output import Output
from .graphviz import GraphvizOutput
from .pickle import PickleOutput
from .ubigraph import UbigraphOutput

outputters = collections.OrderedDict([
    ('graphviz', 'GraphvizOutput'),
    ('ubigraph', 'UbigraphOutput'),
    ('pickle', 'PickleOutput'),
])
