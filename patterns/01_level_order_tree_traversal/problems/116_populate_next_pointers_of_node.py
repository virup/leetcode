# 116. Populating Next Right Pointers in Each Node.
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# This uses the level order tree pattern.

import collections
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = collections.deque([root])
        while len(queue) > 0:
            numnodes = len(queue)
            prevNode = None
            for i in range(0, numnodes):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Check if this is the first node in the level.
                if prevNode is None:
                    prevNode = node
                else:
                    prevNode.next = node

                    # Make the current node prev so that next node cannot be attached
                    # to this.
                    prevNode = node
        return root