# 993. Cousins in Binary Tree.
# https://leetcode.com/problems/cousins-in-binary-tree/
#
# This uses the level order tree pattern.

# Definition for a binary tree node.

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if root is None:
            return False

        # Initialize the parents of x and y as NONE. If found they will captured.
        # The goal of the problem is to find them and make sure that they are not
        # equal and are in same level.
        px, py = None, None
        queue = collections.deque([root])
        while len(queue) > 0:
            numnodes = len(queue)
            for i in range(0, numnodes):
                node = queue.popleft()
                if node.left:
                    if node.left.val == x:
                        px = node
                    if node.left.val == y:
                        py = node
                    queue.append(node.left)
                if node.right:
                    if node.right.val == x:
                        px = node
                    if node.right.val == y:
                        py = node
                    queue.append(node.right)

            # At the end of the level. Check the following.
            # If both px and py are None, parents of the required nodes are not in this
            # level yet.
            # If one of px or py is not None, we have hope of finding the answer.
            # Then check if both px and py are not None. If one of them is None, then
            # parents should not be None and they are not equal.
            if px is not None or py is not None:
                return px is not None and py is not None and px != py

        return False