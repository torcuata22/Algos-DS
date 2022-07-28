#array of integers and positive integer. Find and print the number of (i,j) pairs where
#i<j and array[i] + array[j] is divisible by k
def divisibleSumPairs(n,k,ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k ==0:
                count +=1
    return count 