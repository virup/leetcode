# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Store the current max level
        maxLevel = 0

        # Handle the case with None root
        if root is None:
            return maxLevel

        # Create a double ended queue.
        # The contains a list object with root node. The queue is list of tree nodes.
        queue = collections.deque([root])

        while len(queue) > 0:
            # Increment for new level
            maxLevel += 1

            # The queue at this point contains all the nodes at a given level.

            # length of the queue at each level
            levelLen = len(queue)

            # store all the nodes of the next level of the tree in this list
            level = []

            # Iterate over all the elements in this level
            for i in range(0, levelLen):

                # using popleft() since we are using a deque
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Store the node values of this level in this list
                level.append(node.val)

        return maxLevel