from rr_rank import rr_rank
from item import Item
import random


def test_empty():
    """Empty input should produce empty output"""
    x = rr_rank([])
    assert [] == x


def test_single():
    """With single input, this should be an identity function"""
    results = [[Item("a", 1, None)]]
    x = rr_rank(results=results)
    assert x == [Item("a", 1, None)]


def test_two_same_cg():
    """With two inputs from same CG"""
    results = [[Item("a", 1, None), Item("b", 0.9, None)]]
    x = rr_rank(results=results)
    assert x == [Item("a", 1, None), Item("b", 0.9, None)]


def test_two_diff_cg():
    """With two inputs from same CG"""
    results = [[Item("a", 1, None)], [Item("b", 10, None)]]
    random.seed(4)
    x = rr_rank(results=results)
    assert x == [Item("a", 1, None), Item("b", 10, None)]
