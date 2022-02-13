# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Pattern:
# We use Bottom up DFS for this. In this height is computed in terms of number of nodes.
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # If root is empty, do nothing.
        if root is None:
            return 0

        # DFS to compute height.
        def dfs(node):

            # If the node is leaf node, return 1.
            if len(node.children) == 0:
                return 1

            height = 0
            for child in node.children:
                if child:
                    height = max(height, 1 + dfs(child))

            return height

        return dfs(root)



