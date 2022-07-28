#returnnthe height of a binary tree as an integer.
#If the tree has single node, the height is 0
#Height of the tree = number of edges (lines connecting nodes)
#Base case: no node, we return 0; Else: return maximum height of left OR right plus 1 (to account for current node)

def height(root):
    if root is None:
        return -1 #because the root is null
    else:
        return 1 + max(height(root.left), height(root.right))