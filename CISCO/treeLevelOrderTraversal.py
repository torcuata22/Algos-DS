#Given root of the tree, return level order of its node values (l to r and level by level)
#return each level as a list. Algorithm: Breadth First Search (see my notes for implementation)
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range (qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(level)
        return res    
            
                    
                
