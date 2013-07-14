from .output import Output
from .graphviz import GraphvizSourceOutput
from .graphviz import GraphvizImageOutput
from .pickle import PickleOutput

outputters = [
    GraphvizSourceOutput,
    GraphvizImageOutput,
    PickleOutput,
]
