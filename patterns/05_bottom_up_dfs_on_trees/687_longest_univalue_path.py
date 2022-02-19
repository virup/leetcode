# https://leetcode.com/problems/longest-univalue-path/
# Pattern:
# We use Bottom up DFS for this. In this height is computed in terms of number of nodes.
# Definition for a Node.

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        maxDiameter = [0]

        def dfs(node, maxDiameter):
            # If the node does not exist, height is zero.
            if node is None:
                return 0

            # For leaf node height is 1. The answer here is about longest path. So for leaf node
            # the longest path is zero.
            if node.left is None and node.right is None:
                return 1

            # Get the left height. If the height is more than 1, it means, left height is coming with a chain
            # of univalue nodes.
            lh = dfs(node.left, maxDiameter)

            # Get the right height. If the height is more than 1, it means right height is coming with a chain
            # of univalue nodes.
            rh = dfs(node.right, maxDiameter)

            # If the left node exists and current node value does not match with left subtree's longest chain,
            # the left height is useless.
            if node.left and node.val != node.left.val:
                lh = 0

            # If the right node exists and current node value does not match with right subtree's longest chain,
            # the right height is useless.
            if node.right and node.val != node.right.val:
                rh = 0

            # The current height at this point
            ch = max(lh, rh) + 1

            maxDiameter[0] = max(maxDiameter[0], lh + rh)
            return ch

        dfs(root, maxDiameter)
        return maxDiameter[0]
