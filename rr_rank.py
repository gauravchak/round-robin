"""round robin ranker"""
from dataclasses import dataclass
from typing import List
from item import Item


@dataclass
class RRItem:
    """Item with a feature for round robin ranking"""

    item: Item
    rank_feature: float


def rr_rank(results: List[List[Item]]) -> List[Item]:
    """round robin ranker"""
    return []
