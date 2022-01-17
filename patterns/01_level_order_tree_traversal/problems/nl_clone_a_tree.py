# Clone a tree given and return the root of new tree.
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
    def Clone(self, root: Optional[TreeNode]):

        root2 = TreeNode(root.val)
        queue = collections.deque([root, root2])
        while len(queue) > 0:
            numnodes = len(queue)
            for i in range(0, numnodes):
                node1, node2 = queue.popleft()
                if node1.left:
                    node2.left = TreeNode(node1.left.val)
                    queue.append((node1.left, node2.left))
                if node1.right:
                    node2.right = TreeNode(node2.right.val)
                    queue.append((node1.right, node2.right))

        return root2