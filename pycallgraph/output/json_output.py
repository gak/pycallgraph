import json

from .output import Output


class JsonOutput(Output):

    def __init__(self):
        self.fp = None
        self.output_file = 'pycallgraph.json'

    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()

        subparser = subparsers.add_parser(
            'json',
            help='Dump trace to a JSON file',
            parents=[parent_parser], usage=usage,
        )

        subparser.add_argument(
            '-o', '--output-file', type=str, default=defaults.output_file,
            help='The generated JSON file',
        )

        return subparser

    def done(self):
        self.prepare_output_file()
        out = {
            'groups': self.generate_groups(),
            'nodes': self.generate_nodes(),
            'edges': self.generate_edges(),
        }

        json.dump(out, self.fp)
        self.fp.close()

    def generate_nodes(self):
        nodes = {}
        for node in self.processor.nodes():
            nodes[node.name] = {
                'name': node.name,
                'calls': node.calls.value,
                'time': node.time.value,
            }
        return nodes

    def generate_edges(self):
        edges = []
        for edge in self.processor.edges():
            edges.append({
                'src_func': edge.src_func,
                'dst_func': edge.dst_func,
                'calls': edge.calls.value,
            })
        return edges

    def generate_groups(self):
        groups = {}
        for group, funcs in self.processor.groups():
            funcs = [f.name for f in funcs]
            groups[group] = funcs
        return groups
