class newNode:
# Constructor to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0
 
# function to print left view of
# binary tree
def printLeftView(root):
    if (not root):
        return
    
    q = []
    q.append(root)
 
    while (len(q)):
        # to determine number of nodes at current level
        n = len(q)
 
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
 
            # Print the left most element at the level:
            if (i == 1):
                print(temp.data, end=" ")
 
            # Add the left node to the queue:
            if (temp.left != None):
                q.append(temp.left)
 
            # Add right node to queue
            if (temp.right != None):
                q.append(temp.right)
                
#Method 2:
# Tree Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# function to get the left view of binary tree
def leftView(root):
    ans = []
 
    if not root:
        return ans
 
    q = []
    q.append(root)
    q.append(None)
    ok = True
 
    while len(q) != 0:
        it = q[0]
        del q[0]
        if it == None:
            if ok == False:
                ok = True
            if len(q) == 0:
                break
 
            else:
                q.append(None)
 
        else:
            if ok:
                ans.append(it.data)
                ok = False
 
            if it.left != None:
                q.append(it.left)
            if it.right != None:
                q.append(it.right)
 
    return ans