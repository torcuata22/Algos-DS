#Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.
#Pico y pala: iterate through array and count how many times each number appears, and build dictionary
#iterate through dictionary, 
#pythonic way: use Counter from collections

# from collections import Counter
# x = Counter({'a':5, 'b':3, 'c':7})
# sorted(x, key=x.get, reverse=True)
# ['c', 'a', 'b']

from collections import Counter

def arraySort(nums):
    c = Counter(nums)
    print(sorted(nums, reverse=True, key=lambda x: (-c[x],x)))

    
n = [10,35,51,44,22,11,21,21,10,10]
arraySort(n)


    