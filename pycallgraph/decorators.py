import functools

from .pycallgraph import PyCallGraph


def trace(output=None, config=None):
    def inner(func):
        @functools.wraps(func)
        def exec_func(*args, **kw_args):
            with(PyCallGraph(output, config)):
                return func(*args, **kw_args)

        return exec_func

    return inner
