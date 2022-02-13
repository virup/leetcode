# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Pattern:
# We use Bottom up DFS for this. In this height is computed in terms of number of nodes.
# Definition for a Node.
from typing import Optional

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def dfs(node):

            # Base case.
            # If the node is leaf node, return 1 since we are calculating
            # height based on node.
            if root.left is None and root.right is None:
                return 1

            lheight = 0
            rheight = 0
            if node.left:
                lheight = dfs(node.left)
            if node.right:
                rheight = dfs(node.right)

            return max(lheight, rheight) + 1

        return dfs(root)