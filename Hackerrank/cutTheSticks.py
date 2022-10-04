#Given a number of sticks n, pick the shortest, cut the others a section the same size as the shortest, and discard it
#after every iteration, record the number of sticks left in the bunch
#until there are none left

from collections import Counter

def cutTheSticks(arr):
    result = []
    n = len(arr)
    s = Counter(arr) #creates dictionary of unique keys with count of each key as value (but we need key, not value!)
    #We need to sort s because we need shortest stick first for each iteration
    for i in sorted(s.keys()):
        result.append(n) #number of sticks before we cut them (in the iteration)
        n -= s[i] #this is the "cutting and discarding" part
    return result

