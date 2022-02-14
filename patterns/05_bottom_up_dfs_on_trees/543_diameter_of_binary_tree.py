# https://leetcode.com/problems/diameter-of-binary-tree/
# Pattern:
# We use Bottom up DFS for this. In this height is computed in terms of number of nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Option 1:
#
# Return both height and diameter as a tuple.
#
# The tricky part here is
# Height is calculated as function of number of nodes in the path.
# Diameter is calcluated as edges length.
#
# 1. For null node, return height and diameter as zero since there are zero nodes and zero edges.
#
# 2. For a leaf node, height = 1 since its based on number of nodes and diamater as zero since it is based on number
#    edges.
#
# 3. For a non leaf node, there are three cases
#
# Case 1:
#                 1
#                    2
#
#
# . left heigh = 0
# . left diamater = 0
# . right height = 1 (num nodes)
#  right diameter = 0 (num nodes)
#
# . current height = 2
# . current diameter = 1 (1->2 edge)
#  Ans : 1

# Case 2:
#                 1
#              2
#
# left height = 1
# left diameter = 0
# right height = 0
# right diameter = 0
#
# current height = 2
# current diamater = 1
# Ans: 1
#
# Case 3:
#                 1
#              2     3
#
# left height = 1
# left diameter = 0
# right height = 1
# right diameter = 0

# current height = 2 (1->2 or 1->3)
# current diameter = lh + rh = 2
# Note that to get diameter we can simply add left height and right height.
#
# Note that since height is based out of nodes, when we are calculating diameter that is passing the current node
# lh+rh is sufficient. This is because lh brings an additional count. So we dont need add +1 for the edge. Same with
# right height.

from typing import Optional

class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None:
                return (0, 0)

            if node.left is None and node.right is None:
                return (1, 0)

            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)

            cd = max(ld, rd, lh + rh)

            return max(lh, rh) + 1, cd

        h, d = dfs(root)
        return d
