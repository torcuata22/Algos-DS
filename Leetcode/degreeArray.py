#find length of shorter subarray containing max number of repeated elements
#find shortest subarray containing all repeated numbers

from collections import Counter


def arrayDegree(nums):
    c=Counter(nums) 
    count = max(c.values())
    print (count)
    
numbers = [1,2,3,2,2,4,5,7,6,2,]
#arrayDegree(numbers)
            
        
#For degree and length of shortest subarray containing repeated numbers:


def findShortestSubArray( nums):
    left, right, count = {}, {}, {} #initialize three empty dicts
    for i, x in enumerate(nums): #enumerate generates object with a counter, i=index and x=value
        if x not in left: 
            left[x] = i
        right[x] = i
        count[x] = count.get(x, 0) + 1 #get() is a dictionary method takes key name (mandatory) and value(optional)count the number of occurrences of each character: if it already has a count for a given character, get returns it (so it's just incremented by one), else get returns 0 (so the incrementing correctly gives 1 at a character's first occurrence in the string).

    ans = len(nums)
    degree = max(count.values())
    for x in count:
        if count[x] == degree:
            ans = min(ans, right[x] - left[x] + 1)

    print(ans)

findShortestSubArray(numbers)