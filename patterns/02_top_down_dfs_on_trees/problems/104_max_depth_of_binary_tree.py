# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
#
# This uses the top down dfs pattern.
#
# Definition for a binary tree node.
from typing import  Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check if root is None.
        if root is None:
            return 0

        # The output reference variable.
        output = [0]

        # The inner function. This is the recursive dfs call.
        def dfs(node, level, output):
            # This is current level.
            level = level + 1

            # If we are at lef node, check if we have obtained a max height.
            if node.left is None and node.right is None:
                output[0] = max(output[0], level)

            # Run DFS on left node.
            if node.left:
                dfs(node.left, level, output)

            # Run DFS on right node.
            if node.right:
                dfs(node.right, level, output)

        # Start the DFS.
        dfs(root, 0, output)
        return output[0]
