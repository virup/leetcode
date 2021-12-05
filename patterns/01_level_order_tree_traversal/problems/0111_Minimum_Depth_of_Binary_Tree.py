# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# This uses the level order tree pattern.

import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # min level is stored here
        minLevel = 0

        if root is None:
            return minLevel

        # Create a double ended queue.
        # The contains a list object with root node. The queue is list of tree nodes.
        queue = collections.deque([root])

        while len(queue) > 0:
            minLevel += 1
            # The queue at this point contains all the nodes at a given level.
            levelLen = len(queue)
            for i in range(0, levelLen):
                node = queue.popleft()
                # if node is leaf (no child), then return level
                if node.left is None and node.right is None:
                    return minLevel
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return minLevel
