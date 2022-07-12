#Print top view of binary tree: Print only top nodes you'd see if looking at tree from the top
#Use recursion (to traverse), a dictionary to store positions as keys, root position = 0, then 
#left position = -1 and right position = +1, I will also store the minimum level of the node 
def topView(root):
    #create dictionary to hold key values:
    d={}
    #create a function to traverse tree, use recursion:
    def traverse(root, key, level):
        if key not in d:
            d[key] = [root, level]
        #if key is in d, but the level stored is greater than the current level:
        elif d[key][1]>level:
            d[key]=[root, level] #save new level
        
    #use recursion to traverse the tree, storing the keys and levels as needed
        traverse (root.left, key-1, level+1)
        traverse (root.right, key+1, level+1)
        