# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
#
from collections import Counter
from typing import List

class Solution:
    from collections import Counter
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCand = sorted(candidates)
        counter = Counter(sortedCand)
        res = []
        findTarget(counter, target, 0, [], res)
        return res


def findTarget(counter, target, lowest, currRes, res):
    if target == 0:
        res.append(currRes)

    for k in counter:
        if counter[k] > 0 and k <= target and k >= lowest:
            counter[k] -= 1
            lowest = k

            ccRes = currRes.copy()
            ccRes.append(k)
            findTarget(counter, target - k, lowest, ccRes, res)
            counter[k] += 1

