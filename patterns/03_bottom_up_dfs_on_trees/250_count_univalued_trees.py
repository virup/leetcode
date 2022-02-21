# https://leetcode.com/problems/count-univalue-subtrees/
# Pattern:
# We use Bottom up DFS for this.
# Definition for a Node.

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        # If no root is provided, return 0 as the number of univalued trees.
        if root is None:
            return 0

        counter = [0]

        def dfs(node, counter):

            # For null node return TRUE for higher up AND conditions but no need to
            # increment the counter.
            if node is None:
                return True

            # Leaf node is always univalued.
            if node.left is None and node.right is None:
                counter[0] = counter[0] + 1
                return True

            # We are non leaf node here.
            lefUnivalued = dfs(node.left, counter)
            rightUnivalued = dfs(node.right, counter)
            amIUnivalued = True
            if node.left and node.left.val != node.val:
                amIUnivalued = False
            if node.right and node.right.val != node.val:
                amIUnivalued = False

            if lefUnivalued and rightUnivalued and amIUnivalued:
                counter[0] = counter[0] + 1
                return True

            return False

        dfs(root, counter)
        return counter[0]

