#Insertion Sort Algorithm: 
#need to move elements or array ascending order, so check key = arr[i], if element in array is > key, it
#moves one position ahead of current position

def insertionSort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        print (key)
        j=i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    print (arr)
            
a=[12,11,13,5,6]
insertionSort(a)
