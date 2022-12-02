"""round robin ranker"""
from dataclasses import dataclass
from typing import List
from item import Item
from random import shuffle


@dataclass
class RRItem:
    """Item with a feature for round robin ranking"""

    item: Item
    rank_feature: float


def rank_to_feature(rank: int) -> float:
    """Converts the rank into a float value to be used in round robin ranking."""
    return 1 / float(max(1, rank))


def generate_offsets(numlists: int) -> List[float]:
    """These offsets are used by the round robin ranker to maintain the same order of"""
    offsets = [0.0] * numlists

    for i in range(1, len(offsets)):
        offsets[i] = offsets[i - 1] + 0.001
        # 0.001 is small emnough to not interfere with rr ranking since result-lists
        # should contain less than 100 items.

    # random shuffling ensures that we are being fair to CGs and each CG is getting an
    # equal chance of being at rank 1 even under round-robin ranking.
    shuffle(offsets)
    return offsets


def rr_rank(results: List[List[Item]]) -> List[Item]:
    """round robin ranker"""
    rr_items: List[RRItem] = []
    id_to_idx: dict = {}
    offsets = generate_offsets(len(results))
    for res_idx, ranklist in enumerate(results):
        for item_idx, item in enumerate(ranklist):
            if item.id not in id_to_idx:
                # item has not been seen in any other candidate generator so far
                idx = len(rr_items)
                rr_item = RRItem(item, rank_to_feature(item_idx + 1) + offsets[res_idx])
                rr_items.append(rr_item)
                id_to_idx[item.id] = idx
            else:
                rr_items[id_to_idx[item.id]].rank_feature += (
                    rank_to_feature(item_idx + 1) + offsets[res_idx]
                )
                if (
                    rr_items[id_to_idx[item.id]].item.cg1_feature is None
                    and item.cg1_feature is not None
                ):
                    rr_items[id_to_idx[item.id]].item.cg1_feature = item.cg1_feature
                if (
                    rr_items[id_to_idx[item.id]].item.cg2_feature is None
                    and item.cg2_feature is not None
                ):
                    rr_items[id_to_idx[item.id]].item.cg2_feature = item.cg2_feature

    rr_items.sort(key=lambda x: x.rank_feature, reverse=True)
    return [x.item for x in rr_items]
