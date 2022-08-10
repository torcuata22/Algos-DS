#print the tree level by level instead of nodes. For this, use queue, this way we cna explore all levels

from collections import deque
def levelOrder(root):
    q = deque([root])
    #as long as there are elements in q
    while len(q):
        root = q.popleft() #remove the first element of the queue
        print(root, end=" ")
        if root.left:#append left element if there is one
            q.append(root.left)
        if root.right: #append right element if there is one
            q.append(root.right)
            
        #this will repeat until len(q)=0