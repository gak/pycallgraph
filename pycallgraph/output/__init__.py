from .output import Output
from .graphviz import GraphvizSourceOutput
from .graphviz import GraphvizImageOutput

outputters = [
    GraphvizSourceOutput,
    GraphvizImageOutput,
]
