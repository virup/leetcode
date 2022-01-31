# 216. Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/
#
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        combSumRecursive(1, n, k, [], res)
        return res


def combSumRecursive(lowest, target, tries, currRes, res):
    if target < 0:
        return

    if target == 0 and tries == 0:
        res.append(currRes)

    for i in range(lowest, 10):
        if i <= target:
            cRes = currRes.copy()
            cRes.append(i)
            combSumRecursive(i + 1, target - i, tries - 1, cRes, res)
