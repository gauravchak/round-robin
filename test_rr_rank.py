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
    """With two inputs from same CG, depending on the random shuffle, each can be at rank 0"""
    results = [[Item("a", 1, None)], [Item("b", 10, None)]]

    random.seed(4)
    x = rr_rank(results=results)
    assert x == [Item("a", 1, None), Item("b", 10, None)]

    random.seed(5)
    x = rr_rank(results=results)
    assert x == [Item("b", 10, None), Item("a", 1, None)]


def test_three_items_two_cg():
    """With three items"""
    results = [
        [
            Item("a1", 1, None),
            Item("a2", 0.9, None),
        ],
        [Item("b1", None, 10)],
    ]

    random.seed(4)
    x = rr_rank(results=results)
    assert x == [Item("a1", 1, None), Item("b1", None, 10), Item("a2", 0.9, None)]


def test_overlapping_items():
    """Overlapping items"""
    results = [
        [
            Item("a1", 1, None),
            Item("a2", 0.95, None),
            Item("ac", 0.9, None),
        ],
        [Item("b1", None, 10), Item("ac", None, 9)],
    ]

    random.seed(4)
    x = rr_rank(results=results)
    assert x == [
        Item("a1", 1, None),
        Item("b1", None, 10),
        Item("ac", 0.9, 9),
        Item("a2", 0.95, None),
    ]
