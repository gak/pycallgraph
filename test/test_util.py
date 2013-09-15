from helpers import *


def test_human_readable_biyte():
    hrb = Util.human_readable_bibyte
    assert hrb(0) == '0.0B'
    assert hrb(1024) == '1.0KiB'
    assert hrb(1024 * 5.2) == '5.2KiB'
    assert hrb(1024 * 1024 * 5.2) == '5.2MiB'
    assert hrb(1024 * 1024 * 1024 * 5.2) == '5.2GiB'
    assert hrb(1024 * 1024 * 1024 * 1024 * 5.2) == '5.2TiB'
    assert hrb(1024 * 1024 * 1024 * 1024 * 1024 * 5.2) == '5324.8TiB'
    assert hrb(-1024 * 1024 * 1024 * 5.2) == '-5.2GiB'
    assert hrb(-1024) == '-1.0KiB'
