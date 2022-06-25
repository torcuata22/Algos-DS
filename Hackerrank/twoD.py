import math

def hourglassSum(arr):
    maxSum = -63
    for i in range(4):
        for j in range(4):
            # sum of top 3 elements
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            
            # sum of the mid element
            mid = arr[i+1][j+1]
            
            # sum of bottom 3 elements
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            
            hourglass = top + mid + bottom
            
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum
    
    