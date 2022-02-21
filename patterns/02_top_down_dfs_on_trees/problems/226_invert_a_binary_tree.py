# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
#
# This uses the top down dfs pattern.
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Bail out if the original tree is empty.
        if root is None:
            return

        # The inner function. This is the actual DFS function.
        def dfs(node):
            # If it is leaf node, do nothing.
            if node.left is None and node.right is None:
                pass

            # Swap the left node and right node pointers. This can be done after the dfs too.
            node.left, node.right = node.right, node.left

            # Call the dfs on the left node.
            if node.left:
                dfs(node.left)

            # Call the dfs on the right node.
            if node.right:
                dfs(node.right)

        dfs(root)
        return root