#see leetcode 981 for problem and neetcode for explanation

def __init__(self):
    self.store={}
    
def set(self, key:str, value:str, timestamp:int) -> None:
    if key not in self.store:
        self.store[key] = []
    self.store[key].append([value, timestamp])
    
def get(self, key:str, timestamp:int) ->str:
    res = ''
    values = self.store.get(key,[])
    
    #binary search:
    l,r = 0, len(values)-1
    while l <= r:
        m=(l+m)//2
        if values[m][1] <= timestamp:
            res = values[m][0]
            l = m + 1
        else:
            r = m - 1
    return res
