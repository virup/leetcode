# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/
#
# This uses the top down dfs pattern.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # Create a reference variable to use in the recursive function.
        output = [0]

        # If it empty tree, there is nothing to do.
        if root is None:
            return output[0]

        # Inner function to do the recursion.
        def dfs(node, slate, targetSum, output):

            # Add the node to slate.
            slate.append(node.val)

            subArraySum = 0
            for i in range(len(slate) - 1, -1, -1):
                subArraySum += slate[i]
                if subArraySum == targetSum:
                    output[0] = output[0] + 1

            # Nothing to do in the case of leaf node.
            if node.left is None and node.right is None:
                pass

            # If left node is present, do the dfs on the left node.
            if node.left:
                dfs(node.left, slate, targetSum, output)

            # If right node is present, do the dfs on the right node.
            if node.right:
                dfs(node.right, slate, targetSum, output)

            # Remove it from slate, once we are done with processing.
            slate.pop()

        dfs(root, [], targetSum, output)
        return output[0]