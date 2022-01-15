# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        toggle = True

        queue = collections.deque([root])
        while len(queue) > 0:
            numnodes = len(queue)
            for i in range(0, numnodes):
                node = queue.popleft()
                if node.left:
                    if not toggle:
                        return False
                    queue.append(node.left)
                else:
                    toggle = False

                if node.right:
                    if not toggle:
                        return False
                    queue.append(node.right)
                else:
                    toggle = False

        return True
