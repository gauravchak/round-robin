# Round Robin Ranking
This is a sample round robin ranking implementation.

## Input
We are given lists of items. Think of items as ranked lists from a [candidate generator](https://developers.google.com/machine-learning/recommendation/overview/candidate-generation).
Each item in list i accrues a weight proportional to `1/pos_i` if the position of the item in that list was `i`.


## Weighted round robin ranking
An improvement of round robin ranking would be weifgted round robin ranking. We are not only given the ranked lists but also weights `w_i` for each ranked list, each candidate generator if you will. This could be the desired distribution of candidate generators in the final ranked list.
```py
def weighted_rr_rank(ranked_lists, cg_weights):
  item_weights = {} # map from item id to final ranking weight
  for list_idx, ranked_list in ranked_lists:
    for pos, item in ranked_list:
      cwt = item_weights.get(item.id, 0)
      item_weights[item.id] = cwt + cg_weights[list_idx]/pos
  x = sorted(item_weights.items(), key=lambda item: item[1], reverse=True)
  returb x
```
