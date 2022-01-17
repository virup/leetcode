# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
#
# This uses the level order tree pattern.

# Definition for a binary tree node.

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        queue = collections.deque([(root, root)])
        while len(queue) > 0:
            numnodes = len(queue)

            for i in range(0, numnodes):
                r1, r2 = queue.popleft()

                if r1 is None and r2 is None:
                    continue

                if r1 is None or r2 is None:
                    return False

                if r1.val != r2.val:
                    return False

                queue.append((r1.left, r2.right))
                queue.append((r1.right, r2.left))

        return True