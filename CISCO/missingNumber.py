#Given array of size n-1, with ints in range (1, n-1), find the missing number from 
#the array from the first n integers. THe array is ordered and there are no duplicate
#values
#My solution, using Gauss' formula has o(1) time complexity

def getMissingNum (arr, n):
    total = n(n+1)/2
    sum = sum(arr)
    missing_number = total - sum
    return missing_number

#From LEETCODE: n distinct numbers in range [0,n], so length of array is n+1
#solution must use  o(1) space and o(n) time complexity
#Method 1: needs binary properties, the x OR operator (exclusive OR) then I 
# array ^ range of numbers --> the repeating numbers cancel each other out and 
#ony missing number remains
#time complexity; o(1)

def getMissingBinary(arr,n):
  diff= arr ^ n
  return diff

#Method 2: sum(range) - sum(array) = missing number
#time complexity: o(2n) because each sum takes o(n) time complexity and o(1) memory
def missing_number(self,nums:list[int])->int:
    res = len(nums)
    for i in range(len(nums)):
        res += (i-nums[i])
    return res 


def MissingNumber(self,array,n):
    sum_n= n*(n+1)//2
    sum_a = sum(array)
    missing = abs(sum_a - sum_n)
    return missing
        