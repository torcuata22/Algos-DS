#Given array of numbers, find longest subarray where abs(a[i]-a[j]) <= 1
#use Counter from module collections, as a Counter is a container that stores elements as dictionary 
# keys, and their counts are stored as dictionary values.
from collections import Counter
def pickingNumbers(a):
    countNums=Counter(a)
    maxnum=0
    for i in range(1,100):
        maxnum = max(maxnum, countNums[i]+countNums[i+1])
    return maxnum
