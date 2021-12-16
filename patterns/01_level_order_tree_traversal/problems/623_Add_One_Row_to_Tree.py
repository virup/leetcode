# 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/
#
# This uses the level order tree pattern.

import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        # Case where d == 1. In this case attach the given root node as the left
        # node.
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        level = 0
        queue = collections.deque([root])
        while len(queue) > 0:
            level = level + 1
            numnodes = len(queue)
            for i in range(0, numnodes):
                node = queue.popleft()

                if level >= d:
                    break

                if level == d - 1:
                    newnode = TreeNode(v)
                    temp = node.left
                    node.left = newnode
                    newnode.left = temp
                    newnode = TreeNode(v)
                    temp = node.right
                    node.right = newnode
                    newnode.right = temp

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
