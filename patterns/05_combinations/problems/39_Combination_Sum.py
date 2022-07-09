# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
#
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        findTargetSum(candidates, target, 0, [], res)
        return res


def findTargetSum(candidates, targetLeft, first, currRes, res):
    if targetLeft == 0:
        res.append(currRes)

    for i in range(first, len(candidates)):
        num = candidates[i]
        if targetLeft >= num:
            ccRes = currRes.copy()
            ccRes.append(num)
            findTargetSum(candidates, targetLeft -num, i, ccRes, res)
