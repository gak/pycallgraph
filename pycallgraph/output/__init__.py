from .output import Output
from .graphviz import GraphvizOutput
from .pickle import PickleOutput
from .ubigraph import UbigraphOutput

outputters = [
    GraphvizOutput,
    PickleOutput,
    UbigraphOutput,
]
