def miniMaxSum(arr):
    arr.sort() #sort organizes elements in ascending order
    s=sum(arr)
    max = s - arr[0] #because the smallest value is now in index zero
    min = s - arr[len(arr)-1]
    
    print(min, max)
    
    
arr = [1,2,3,4,5]
miniMaxSum(arr)