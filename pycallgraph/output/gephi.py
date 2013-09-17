import math

from .output import Output


class GephiOutput(Output):
    def __init__(self, **kwargs):
        self.fp = None
        self.output_file = 'pycallgraph.gdf'
        Output.__init__(self, **kwargs)

    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()

        subparser = subparsers.add_parser(
            'gephi', help='Gephi GDF generation',
            parents=[parent_parser], usage=usage,
        )

        cls.add_output_file(
            subparser, defaults, 'The generated Gephi GDF file'
        )

    def generate(self):
        '''Returns a string with the contents of a GDF file.'''

        return u'\n'.join([
            self.generate_nodes(),
            self.generate_edges(),
        ]) + '\n'

    def generate_nodes(self):
        output = []

        fields = u', '.join([
            u'name VARCHAR',
            u'label VARCHAR',
            u'group VARCHAR',
            u'calls INTEGER',
            u'time DOUBLE',
            u'memory_in INTEGER',
            u'memory_out INTEGER',
            u'color VARCHAR',
            u'width DOUBLE',
        ])
        output.append(u'nodedef> {}'.format(fields))

        for node in self.processor.nodes():
            fields = u','.join([str(a) for a in [
                node.name,
                node.name,
                node.group,
                node.calls.value,
                node.time.value,
                node.memory_in.value,
                node.memory_out.value,
                u"'{}'".format(self.node_color_func(node).rgb_csv()),
                self.node_size(node),
            ]])
            output.append(fields)

        return '\n'.join(output)

    def node_size(self, node):
        return math.log(node.time.fraction * (math.e - 1) + 1) * 2 + 1

    def generate_edges(self):
        output = []

        fields = u', '.join([
            u'node1 VARCHAR',
            u'node2 VARCHAR',
            u'label VARCHAR',
            u'labelvisible VARCHAR',
            u'directed BOOLEAN',
            u'color VARCHAR',
            u'width DOUBLE',
        ])
        output.append(u'edgedef> {}'.format(fields))

        for edge in self.processor.edges():
            fields = u','.join([str(a) for a in [
                edge.src_func,
                edge.dst_func,
                self.edge_label(edge),
                'true',
                'true',
                u"'{}'".format(self.edge_color_func(edge).rgb_csv()),
                edge.calls.fraction * 2,
            ]])
            output.append(fields)

        return '\n'.join(output)

    def done(self):
        source = self.generate()
        f = open(self.output_file, 'w')
        f.write(source)
        f.close()
