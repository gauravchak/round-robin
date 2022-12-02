from rr_rank import rr_rank
from item import Item


def test_empty():
    """Empty input should produce empty output"""
    x = rr_rank([])
    assert [] == x


def test_single():
    """With single input, this should be an identity function"""
    results = [[Item("abc", 1, None)]]
    x = rr_rank(results=results)
    assert x == [Item("abc", 1, None)]
