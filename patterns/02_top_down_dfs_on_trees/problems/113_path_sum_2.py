# 113. Path Sum
# https://leetcode.com/problems/path-sum-ii/
#
# This uses the top down dfs pattern.
# Definition for a binary tree node.
from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int):

        # The 2D output list.
        output = []

        # Corner case. If root is empty, nothing to return
        if root is None:
            return output

        def dfs(node, slate, sumSoFar):

            sumSoFar = sumSoFar + node.val
            slate.append(node.val)

            # Cannot do any optimization here if sumSoFar is greater
            # than target sum because there could be negative
            # values down the path.

            # Check if it is leaf node.
            if node.left is None and node.right is None:
                if sumSoFar == targetSum:
                    output.append(slate[:])

            if node.left:
                dfs(node.left, slate, sumSoFar)
            if node.right:
                dfs(node.right, slate, sumSoFar)

            # Once the current node is done, pop it.
            slate.pop()

        dfs(root, [], 0)
        return output