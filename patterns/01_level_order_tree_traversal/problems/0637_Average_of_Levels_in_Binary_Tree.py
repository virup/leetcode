# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
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
    def levelOrder(self, root: Optional[TreeNode]) -> [[int]]:

        # Handle the case with None root
        if root is None:
            return None

        # This is the output list
        output = []

        # Create a double ended queue.
        # The contains a list object with root node. The queue is list of tree nodes.
        queue = collections.deque([root])

        # This is a boolean toogle variable to keep track of whether to reverse a
        # level or not. The value is alternated for every level.
        is_reverse = False

        while len(queue) > 0:
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

            # Store the average node values of all the nodes in a level
            output.append(sum(level)/len(level))


        # The output contains the nodes in each level as a list object
        return output

