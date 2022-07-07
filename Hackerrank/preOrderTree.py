#Function must print values in tree's preorder traversal as a single line of space-separated values
#to traverse tree: root.left and root.left (every new node becomes root)
#to print in one line: print(root, end = " ")

def preOrder(root):
    if root != None:
        print (root, end = " ")
    #to traverse to left of root: 
    preOrder(root.left)
    #to traverse to right of root:
    preOrder(root.right)