#Given array of size n-1, with ints in range (1, n-1), find the missing number from 
#the array from the first n integers. THe array is ordered and there are no duplicate
#values

def getMissingNum (arr, n):
    total = n(n+1)/2
    sum = sum(arr)
    missing_number = total - sum
    return missing_number