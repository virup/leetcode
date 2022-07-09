# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# This pattern performs a level order traversal of a binary tree. At
# each level it stores the nodes of the next level in the queue. Before
# iterating over the nodes in the next level, it keeps a record of the
# length of the queue so that it knows when the level is done.

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

            # Store the node
            output.append(level)

        # The output contains the nodes in each level as a list object
        return output
