# 100. Same tree
# https://leetcode.com/problems/same-tree/
#
# This uses the level order tree pattern.

# Definition for a binary tree node.
from typing import Optional
import collections
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Check if both nodes are null.
        if p is None and q is None:
            return True

        # Check if left tree node is not null and right tree root is null.
        if p is not None and not q:
            return False

        # Check if left root is null and right is not.
        if not p and q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while len(queue1) > 0 and len(queue2) > 0:
            numnodes1 = len(queue1)
            numnodes2 = len(queue2)

            # Check if number of nodes in the level are not same.
            # If they are not equal, return false, right away.
            if numnodes1 != numnodes2:
                return False

            for i in range(0, numnodes1):
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                if node1.val != node2.val:
                    return False

                if node1.left and not node2.left:
                    return False

                if not node1.left and node2.left:
                    return False

                if node1.right and not node2.right:
                    return False

                if not node1.right and node2.right:
                    return False

                if node1.left:
                    queue1.append(node1.left)
                if node1.right:
                    queue1.append(node1.right)

                if node2.left:
                    queue2.append(node2.left)
                if node2.right:
                    queue2.append(node2.right)

        # After the traversal is complete, check if atleast one of the queue is empty.
        if len(queue1) > 0 or len(queue2) > 0:
            return False

        return True