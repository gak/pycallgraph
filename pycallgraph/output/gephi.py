from ..metadata import __version__
from ..exceptions import PyCallGraphException
from .output import Output


class GephiOutput(Output):
    def __init__(self):
        self.fp = None
        self.output_file = 'pycallgraph.gdf'


# TODO NEEDS PORTING
# def get_gdf(stop=True):
#     """Returns a string containing a GDF file. Setting stop to True will
#cause
#     the trace to stop.
#     """
#     ret = ['nodedef>name VARCHAR, label VARCHAR, hits INTEGER, ' + \
#             'calls_frac DOUBLE, total_time_frac DOUBLE, ' + \
#             'total_time DOUBLE, color VARCHAR, width DOUBLE,
#total_memory_in_frac DOUBLE, total_memory_in DOUBLE']
#     for func, hits in func_count.items():
#         calls_frac, total_time_frac, total_time, total_memory_in_frac,
#total_memory_in, \
#             total_memory_out_frac, total_memory_out == _frac_calculation(
#func, hits)
#         col = settings['node_colour'](calls_frac, total_time_frac)
#         color = ','.join([str(round(float(c) * 255)) for c in col.split()])
#         if time_filter==None or time_filter.fraction < total_time_frac:
#             ret.append('%s,%s,%s,%s,%s,%s,%s,%s,%s,\'%s\',%s' % (func, func,
#hits, \
#                     calls_frac, total_time_frac, total_time,
#total_memory_in_frac, total_memory_in, total_memory_out, color, \
#                     math.log(hits * 10)))

#     ret.append('edgedef>node1 VARCHAR, node2 VARCHAR, color VARCHAR')
#     for fr_key, fr_val in call_dict.items():
#         if fr_key == '':
#             continue
#         for to_key, to_val in fr_val.items():
#             calls_frac, total_time_frac, total_time, total_memory_in_frac,
#total_memory_in, \
#                total_memory_out_frac, total_memory_out =
#_frac_calculation(to_key, to_val)
#             col = settings['edge_colour'](calls_frac, total_time_frac)
#             color = ','.join([str(round(float(c) * 255))
#for c in col.split()])
#             if time_filter==None or time_filter.fraction < total_time_frac:
#                 ret.append('%s,%s,\'%s\'' % (fr_key, to_key, color))
#     ret = '\n'.join(ret)
#     return ret


# def save_gdf(filename):
#     """Generates a GDF file and writes it into filename."""
#     open(filename, 'w').write(get_gdf())


# def make_gdf_graph(filename, stop=True):
#     """Create a graph in simple GDF format, suitable for feeding into Gephi,
#     or some other graph manipulation and display tool. Setting stop to True
#     will stop the current trace.
#     """
#     if stop:
#         stop_trace()

#     try:
#         f = open(filename, 'w')
#         f.write(get_gdf())
#     finally:
#         if f: f.close()
