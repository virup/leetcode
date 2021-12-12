# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#
# This uses the level order tree pattern.

import collections
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = collections.deque([root])
        maxlevelsum = float("-INF")
        level = 0
        maxlevel = 1
        while len(queue) > 0:
            level = level + 1
            numnodes = len(queue)
            levelsum = 0
            for i in range(0, numnodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levelsum = levelsum + node.val

            if levelsum > maxlevelsum:
                maxlevelsum = levelsum
                maxlevel = level

        return maxlevel