# 112. Path Sum
# https://leetcode.com/problems/path-sum/
#
# This uses the top down dfs pattern.
#
# Note that this problem has one optimization from the pattern. Once a specific path with target
# sum is found, there is no need to traverse other paths since its a boolean problem.

# Definition for a binary tree node.
from typing import Optional
import collections
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # Check if the root node is None.
        if root is None:
            return False

        # Since this will be used in inner function, this variable has to be reference
        # variable.
        ans = [False]

        def dfs(node, target):
            # Optimization. If the answer was found already. No need to find new
            # paths.
            if ans[0]:
                return

            # Base case.
            # If it is leaf node,
            if node.left is None and node.right is None:
                target = target + node.val
                if target == targetSum:
                    ans[0] = True

            if node.left:
                dfs(node.left, target + node.val)

            if node.right:
                dfs(node.right, target + node.val)

        dfs(root, 0)
        return ans[0]