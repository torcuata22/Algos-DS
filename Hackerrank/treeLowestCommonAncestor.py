#v1 always < than v2, if not, I need to swao them (to maintain the condition), and v1 is always different than v2
#if both values are smaller than root.info, go to the left of the root
#if both are greater, go to the right

def lca(root, v1, v2):
    if v1>v2:
        v1, v2 = v2, v1
    while True:
        
        if v1 < root.info and v2 < root.info:
            root=root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root