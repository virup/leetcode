# Problem Statement.
# Height of K ary tree, T containing N nodes. You have to find height of the tree. (Length of the
# longest path from root to any node.). Here we are looking for number of edges on the longest
# path from root to any nodes, not number of nodes on longest path from root to any node.
#
# Pattern
#
# 1. This is opposite of top down DFS where the information flows from top to down.
#
# 2. Propogate the computed values from the child trees.
#
# 3. Do the computation on the current node along with values returned from children. Propogate
#    computation upwards.

def find_height(root):

    # If the root is empty, bail out.
    if root is None:
        return 0

    # Recursive function. Note that we are returning height from each node.
    def dfs(node):
        # If there are no children for this node, return 0 since our height is
        # base on number of edges.
        if len(node.children) == 0:
            return 0

        height = 0
        for child in node.children:
            height = max(height, 1+dfs(child))

        return height

    return dfs(root)


