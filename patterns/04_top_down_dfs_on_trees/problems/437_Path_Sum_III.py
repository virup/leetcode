# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/
#

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        # This variable stores a list of sums ending at a particular
        # node but starting at all the nodes in its ancestor
        ancestorSum = []
        return dfs(root, targetSum, ancestorSum)

# In this recursive function, we accept the current node, the remaining targetSum
# and a list of sums starting at all parent nodes of the root and ending
# at the current node (root).
def dfs(root, targetSum, ancestorSums):
    currentRootVal = root.val

    countOfNodesWithTargetSum = 0
    # Add the value of the current node to the list of the
    # ancestor sum. If any of the ancestor sum equals the targetSum
    # then increase the countOfNodesWithTargetSum.
    for i in range(len(ancestorSums)):
        ancestorSums[i] += currentRootVal
        if ancestorSums[i] == targetSum:
            countOfNodesWithTargetSum += 1

    # The last element in the ancestorSum list is just the value of the
    # current node. If the value of the current node is equal to the
    # target sum, then increase the countOfNodesWithTargetSum too.
    ancestorSums.append(currentRootVal)
    if ancestorSums[-1] == targetSum:
        countOfNodesWithTargetSum += 1

    # Recursively go to the left node and the right node if they are present.
    # We need to send the copies of ancestor sums otherwise we will have to subtract
    # the values of the current sum from them after this function is over.
    if root.left:
        countOfNodesWithTargetSum += dfs(root.left, targetSum, ancestorSums.copy())

    if root.right:
        countOfNodesWithTargetSum += dfs(root.right, targetSum, ancestorSums.copy())

    return countOfNodesWithTargetSum


