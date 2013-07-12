from pycallgraph.output import Output


class GraphvizOutput(Output):

    def make_dot_graph(filename, format='png', tool='dot'):
        '''Creates a graph using a Graphviz tool that supports the dot
        language. It will output into a file specified by filename with the
        format specified.  Setting stop to True will stop the current trace.
        '''
        if stop:
            stop_trace()

        dot_data = get_dot()

        # normalize filename
        regex_user_expand = re.compile('\A~')
        if regex_user_expand.match(filename):
            filename = os.path.expanduser(filename)
        else:
            filename = os.path.expandvars(filename)  # expand, just in case

        if format == 'dot':
            f = open(filename, 'w')
            f.write(dot_data)
            f.close()

        else:
            # create a temporary file to be used for the dot data
            fd, tempname = tempfile.mkstemp()
            with os.fdopen(fd, 'w') as f:
                f.write(dot_data)

            cmd = '%(tool)s -T%(format)s -o%(filename)s %(tempname)s' % locals()
            try:
                ret = os.system(cmd)
                if ret:
                    raise PyCallGraphException( \
                        'The command "%(cmd)s" failed with error ' \
                        'code %(ret)i.' % locals())
            finally:
                os.unlink(tempname)




class GraphvizImageOutput(GraphvizOutput):
    pass

