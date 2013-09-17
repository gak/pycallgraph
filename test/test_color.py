from helpers import *


def test_bad_range():
    with pytest.raises(ColorException):
        Color(0, 5, 0, 0)
    with pytest.raises(ColorException):
        Color(0, 0, -1, 0)


def test_hsv():
    c = Color.hsv(0.1, 0.5, 0.75, 0.25)
    assert c.r is 0.75
    assert abs(c.g - 0.6) < 0.1  # Floating point comparison inaccurate
    assert abs(c.b - 0.375) < 0.1
    assert c.a is 0.25


def test_rgb_csv():
    assert Color(0.3, 0.4, 0.5, 0.6).rgb_csv() == '76,102,127'


def test_str():
    assert str(Color(0.071, 0.204, 0.338, 0.471)) == '<Color #12345678>'
