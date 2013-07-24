from .output import Output
from .graphviz import GraphvizSourceOutput
from .graphviz import GraphvizImageOutput
from .pickle import PickleOutput
from .ubigraph import UbigraphOutput

outputters = [
    GraphvizSourceOutput,
    GraphvizImageOutput,
    PickleOutput,
    UbigraphOutput,
]
