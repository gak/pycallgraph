import math

from ..metadata import __version__
from ..exceptions import PyCallGraphException
from .output import Output


class GephiOutput(Output):
    def __init__(self):
        self.fp = None
        self.output_file = 'pycallgraph.gdf'

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
        '''Returns a string containing a GDF file.'''
        ret = ['nodedef>name VARCHAR, label VARCHAR, hits INTEGER, ' + \
                'calls_frac DOUBLE, total_time_frac DOUBLE, ' + \
                'total_time DOUBLE, color VARCHAR, width DOUBLE,' + \
                'total_memory_in_frac DOUBLE, total_memory_in DOUBLE']

        for func, hits in self.processor.func_count.iteritems():
            calls_frac, total_time_frac, total_time, total_memory_in_frac, \
                total_memory_in, total_memory_out_frac, total_memory_out = \
                self.processor.frac_calculation(func, hits)

        # col = settings['node_colour'](calls_frac, total_time_frac)
        # color = ','.join([str(round(float(c) * 255)) for c in col.split()])
        color = '255,0,255'
        # if time_filter==None or time_filter.fraction < total_time_frac:
        ret.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,\'%s\',%s' % (
            func, func, hits, calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, total_memory_out, color, math.log(hits * 10)))

        ret.append('edgedef>node1 VARCHAR, node2 VARCHAR, color VARCHAR')
        for fr_key, fr_val in self.processor.call_dict.items():
            if fr_key == '':
                continue
            for to_key, to_val in fr_val.items():
                calls_frac, total_time_frac, total_time, total_memory_in_frac, total_memory_in, total_memory_out_frac, total_memory_out = self.processor.frac_calculation(to_key, to_val)
                # col = settings['edge_colour'](calls_frac, total_time_frac)
                # color = ','.join([str(round(float(c) * 255))
                #for c in col.split()])
                color = '255,127,127'

                # if time_filter==None or time_filter.fraction < total_time_frac:
                ret.append('%s,%s,\'%s\'' % (fr_key, to_key, color))

        ret = '\n'.join(ret)
        return ret

    def done(self):
        source = self.generate()
        open(self.output_file, 'w').write(source)
