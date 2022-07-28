#It's a Binary Tree search, which means, the lower values go on the left of the tree and the higher values go on
#the right of the tree, so we traverse: root.left, root, root.right to travel through the tree. This will result
#in the nodes being printed in ascending order

def inOrder(root):
#First, check if the root exists:
    if root:
        inOrder(root.left) #check left of the root
        print(root, end=" ") #print the root value
        inOrder (root.right) #check the right of the root