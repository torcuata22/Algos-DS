#DEsign a class to find the kth largest element in a stream at any point in time
#stream means we can continue to add numbers
#kth largest element in the sorted order (sorted list!)
#Use min hap (DS with sorted property, add/pop, log(n) time. min value 0(n))
#we are only added, never removing.
#WHILE len(heap) > K we pop the minimum  values. We end up with a heap of length K
#made up of the highest values (up to the kth highest value) 
# To find the kth largest number of stream, we look for the min. value in the heap
#when we add a number to the stream, we figure out if it's one of the largest values
#by adding to min heap (heap length k already) and pop minimum
import heapq #need this to create the heap


class KthLargest:
    def __init__(self, k:int, nums: list[int]):
     #minHeap with Kth largest integer
        self.minHeap, self.k = nums, k #array right now to turn into heap:
        heapq.heapify(self.minHeap) 
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) #heappop pops smaller item of the heap
         
        
    def add (self, val: int)->int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
#in min Heap, minimum value always at zero index
        

