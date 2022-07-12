#Given to me:
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)



#WRITTEN BY ME:
#To insert values inthe appropriate position: smaller values go to the left, and greater values go to the right
def insert(self, val):
    newnode = Node(val)
    if self.root is None:
        self.root = newnode
        return self
    cur = self.root
    while cur:
        if val < cur.info:
            if cur.left is None:
                cur.left = newnode
                return
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = newnode
                return
            cur = cur.right
            
#Given to me:
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)