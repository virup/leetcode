# 77. Combinations
# https://leetcode.com/problems/combinations/
#

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        recursiveCombine(n, 0, k, res, [])
        return res


def recursiveCombine(n, start, left, res, current):
    if left == 0:
        res.append(current)

    for i in range(start + 1, n + 1):
        newC = current.copy()
        newC.append(i)
        recursiveCombine(n, i, left - 1, res, newC)