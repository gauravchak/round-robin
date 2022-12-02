"""Test file for rr_rank.py"""
import random
from rr_rank import rr_rank
from item import Item


def test_empty():
    """Empty input should produce empty output"""
    ranked_list = rr_rank([])
    assert [] == ranked_list


def test_single():
    """With single input, this should be an identity function"""
    results = [[Item("a", 1, None)]]
    ranked_list = rr_rank(results=results)
    assert ranked_list == [Item("a", 1, None)]


def test_two_same_cg():
    """With two inputs from same CG"""
    results = [[Item("a", 1, None), Item("b", 0.9, None)]]
    ranked_list = rr_rank(results=results)
    assert ranked_list == [Item("a", 1, None), Item("b", 0.9, None)]


def test_two_diff_cg():
    """With two inputs from same CG, depending on the random shuffle, each can be at rank 0"""
    results = [[Item("a", 1, None)], [Item("b", 10, None)]]

    random.seed(4)
    ranked_list = rr_rank(results=results)
    assert ranked_list == [Item("a", 1, None), Item("b", 10, None)]

    random.seed(5)
    ranked_list = rr_rank(results=results)
    assert ranked_list == [Item("b", 10, None), Item("a", 1, None)]


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
    ranked_list = rr_rank(results=results)
    assert ranked_list == [
        Item("a1", 1, None),
        Item("b1", None, 10),
        Item("a2", 0.9, None),
    ]


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
    ranked_list = rr_rank(results=results)
    assert ranked_list == [
        Item("a1", 1, None),
        Item("b1", None, 10),
        Item("ac", 0.9, 9),
        Item("a2", 0.95, None),
    ]
