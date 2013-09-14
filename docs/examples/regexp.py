#!/usr/bin/env python
import argparse
import re

from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph.output import GraphvizOutput


class RegExp(object):

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--grouped', action='store_true')
        conf = parser.parse_args()

        if conf.grouped:
            self.run('regexp_grouped.png', Config(groups=True))
        else:
            self.run('regexp_ungrouped.png', Config(groups=False))

    def run(self, output, config):
        graphviz = GraphvizOutput()
        graphviz.output_file = output
        self.expression = r'^([^s]).*(.)\2.*\1$'

        with PyCallGraph(config=config, output=graphviz):
            self.precompiled()
            self.onthefly()

    def words(self):
        a = 200
        for word in open('/usr/share/dict/words'):
            yield word.strip()
            a -= 1
            if not a:
                return


    def precompiled(self):
        reo = re.compile(self.expression)
        for word in self.words():
            reo.match(word)

    def onthefly(self):
        for word in self.words():
            re.match(self.expression, word)


if __name__ == '__main__':
    RegExp().main()
