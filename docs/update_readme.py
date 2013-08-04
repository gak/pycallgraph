#!/usr/bin/env python3
'''
This script copies the index.rst page from the Sphinx documentation, modifies
it slightly so refs point to the correct place.
'''
import os
import sys
import shutil


class GithubReadmeMaker(object):

    def __init__(self):
        self.root = os.path.abspath(os.path.dirname(__file__))
        os.chdir(self.root)

    def run(self):
        self.copy()
        rst = open('../README.rst').read()
        rst = self.fix_links(rst)
        open('../README.rst', 'w').write(rst)

    def copy(self):
        shutil.copy('index.rst', '../README.rst')

    def fix_links(self, rst):
        return rst


if __name__ == '__main__':
    GithubReadmeMaker().run()
