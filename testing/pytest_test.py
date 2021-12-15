from ..functions import intersection, union


def test_simple_intersection():
    assert intersection(2, 4, 5, 1, 3, 7, 6, 2) == 4
    assert union(2, 4, 5, 1, 3, 7, 6, 2) == 20
    assert intersection(-3, 1, 3, -1, -1, 3, 1, -3) == 4
    assert union(-4, 1, 4, -1, -1, 4, 1, -4) == 28


def test_no_intersection():
    assert intersection(0, 2, 2, 0, 5, 2, 7, 0) == 0
    assert union(0, 2, 2, 0, 5, 2, 7, 0) == 8
    assert intersection(-1, 2, 0, 0, 0, 2, 1, 0) == 0
    assert union(-1, 2, 0, 0, 0, 2, 1, 0) == 4


def test_one_in_one_intersection():
    assert intersection(0, 4, 4, 0, 1, 3, 3, 1) == 4
    assert union(0, 4, 4, 0, 1, 3, 3, 1) == 16
    assert intersection(0, 5, 5, 0, 0, 3, 3, 0) == 9
    assert union(0, 5, 5, 0, 0, 3, 3, 0) == 25


def test_overlap():
    assert intersection(0, 100, 100, 0, 0, 100, 100, 0) == 10000
    assert union(0, 100, 100, 0, 0, 100, 100, 0) == 10000
