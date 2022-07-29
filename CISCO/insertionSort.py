#Insertion Sort Algorithm: 
#need to move elements or array ascending order, so check key = arr[i], if element in array is > key, it
#moves one position ahead of current position, running time: o(n**2)

def insertionSort(arr):
    for i in range (1, len(arr)): #goes from index 1 to index 5
        key = arr[i]
        j=i-1 #left neighbor (we compare to left neighbor)
        while j >= 0 and key < arr[j]: #key is element to the right of arr[j], so, as long as right element is smaller than left element
            arr[j+1] = arr[j]
            j-=1 #to go further to the left after swap
        arr[j+1]=key
   
            
a=[12,11,13,5,6]
insertionSort(a)
print (a)


