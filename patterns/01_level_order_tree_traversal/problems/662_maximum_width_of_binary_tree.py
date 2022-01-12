# 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/
#
# This uses the level order tree pattern.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = collections.deque([(root, 1)])

        maxWidth = float("-INF")
        while len(queue) > 0:
            numnodes = len(queue)
            first = None
            node = None

            for i in range(0, numnodes):

                node, val = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * val))
                if node.right:
                    queue.append((node.right, 2 * val + 1))

                end = val
                if first is None:
                    first = val

                width = end - first + 1
                if width > maxWidth:
                    maxWidth = width
        return maxWidth