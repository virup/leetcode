# https://leetcode.com/problems/diameter-of-binary-tree/
# Pattern:
# We use Bottom up DFS for this. In this height is computed in terms of number of nodes.
# Definition for a binary tree node.

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        diameter = [0]

        def dfs(node):

            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 1

            lh = dfs(node.left)
            rh = dfs(node.right)

            diameter[0] = max(diameter[0], lh + rh)
            return max(lh, rh) + 1

        dfs(root)
        return diameter[0]
