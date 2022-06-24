

def reverse_array(arr):
    n=len(arr)-1
    return arr[n:: -1]

#I am slicing here and using negative indexing. The notation is arr[start:stop:step]
#in this case, it's arr[n::-1]
#n is the starting point the empty space between : and : represents the starting point
#steps can be negative, meaning we're going "backwrds" as it were (-1)
    
       
    
       
       
arr=[1,4,5]
reverse_array(arr)
