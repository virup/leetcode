# 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
#
# This uses the level order tree pattern.

import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # If there are no nodes in the root exit.
        if root is None:
            return 0

        # The max level.
        maxlevel = 0

        # Create a deque with root as the only element.
        queue = collections.deque([root])

        # Until the queue is empty, do the BFS.
        while len(queue) > 0:
            numnodes = len(queue)
            maxlevel = maxlevel + 1
            for i in range(0, numnodes):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)

        return maxlevel
