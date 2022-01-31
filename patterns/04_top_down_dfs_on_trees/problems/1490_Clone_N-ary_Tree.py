# 1490. Clone N-ary Tree
# https://leetcode.com/problems/clone-n-ary-tree/
#


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        return clone(root) # Simple dfs


def clone(root):
    if root is None:
        return None

    clonedChildren = []

    for c in root.children:
        clonedChildren.append(clone(c))

    clonedRoot = Node(root.val, clonedChildren)
    return clonedRoot

