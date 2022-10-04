#print tree in post order traversal: from left to right and bottom to top, ending with the root
#we are inverting the order of treePrePrder exercise, so we begin with root.left, move on to root.roght, and end in root
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print (root, end=" ")