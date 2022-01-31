# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/
# In this problem, we have to capture all the paths in a given binary tree.
# Pattern:
#
# 1. If the root node is empty, there is nothing to run dfs on. Return.
#
# 2. Define a dfs inner function. This is the recursive function.
#
# 3. If the node under action is leaf node, solve the problem for leaf node and exit. Do not run
#    dfs on null cases.
#
# 4. If the left subtree is not null, call the dfs on the left subtree.
#
# 5. If the right subtre is not null, call the dfs on the right subree.
#
# 6. Every time we call the a subproblem on the left side or right side, we reduce the problem.
#
# 7. The current node solves a portion of the problem and delegates the a subset of the problem on
#    the subordinates.
#
# 8. In the recursion we never check if the node is null. Instead we check if the node is leaf node
#    checking if the node.left is None and node.right is None. This is to make sure that we handle
#    the leaf node seperately. For example in this question we want to know if the node is leaf node.
#
# Note that any problem that can be solved with top down DFS can also be solved with BFS.
# Definition for a binary tree node.

import collections
from typing import Optional
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]):

        output = []

        # Handle the case where the root node is None, return empty list.
        if root is None:
            return output

        def dfs(node, slate):

            # Append the value of node.
            slate.append(str(node.val))

            # If its leaf node, append the slate to the result.
            if node.left is None and node.right is None:
                # Note that we are cloning the slate and appending to the
                # output. If we dont do this, we are appending same slate
                # again and again. The slate here is reference. So its
                # important to clone it and append the result to the output.
                output.append("->".join(slate[:]))

            # Run dfs on left node if left node is not empty.
            if node.left is not None:
                # Perform the dfs on the left sub tree.
                dfs(node.left, slate)

            # Run dfs on right node if right node is not empty.
            if node.right is not None:
                # Perform the dfs on the right sub tree.
                dfs(node.right, slate)

            # Once the left and right subree are complete, this means all the paths
            # that includes the current node are done. Remove the current node from
            # the slate before returning to the parent node.
            slate.pop()

        # Call DFS from root node with empty slate.
        dfs(root, [])

        # If we are here, dfs has run to completion and all the paths are captured in the
        # output.
        return output



