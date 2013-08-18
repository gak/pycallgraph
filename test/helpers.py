# flake8: noqa
import time

import pytest

import fix_path
from pycallgraph import *
from pycallgraph.tracer import *
from pycallgraph.output import *


def wait_100ms():
    time.sleep(0.1)


def wait_200ms():
    time.sleep(0.2)
