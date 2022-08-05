#find length of shorter subarray containing max number of repeated elements
#find shortest subarray containing all repeated numbers

from collections import Counter


def arrayDegree(nums):
    c=Counter(nums) 
    count = max(c.values())
    print (count)
    
numbers = [1,2,3,2,2,4,5,7,6,2,]
arrayDegree(numbers)
            
        

