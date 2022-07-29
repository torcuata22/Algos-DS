#Given an array, check if it is a Binary Max Heap
#mid point of array: (n-1)/2
def isHeap(arr, i,n):
    if i >= int((n-1)/2): #returns true if it's a maxHeap
        return True
#if internal node and greater than its children, and same is recursively true for children:
    if (arr[i] >=arr[2*i + 1] and arr[i] >=arr[2*i + 2] and isHeap(arr[2*i+1], n) and isHeap (arr[2*i+2], n)):
        return True
    return False