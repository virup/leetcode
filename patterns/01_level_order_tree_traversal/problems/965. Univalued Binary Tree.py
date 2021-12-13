# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/
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
    def isUnivalTree(self, root: TreeNode) -> bool:

        uniqueVal = root.val

        queue = collections.deque([root])
        while len(queue) > 0:
            numNodes = len(queue)
            for i in range(0, numNodes):
                node = queue.popleft()
                if node.val != uniqueVal:
                    return False

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return True
