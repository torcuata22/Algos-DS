import heapq

a=[52, 94, 13, 77, 41]
heapq.heapify(a) #do not create new variable, you are rearranging original list into heap
#print(a)

heapq.heappush(a,10) #pushes 10 to index 0 because it is the smallest value
#print(a)

#print(heapq.heappop(a)) #pops 10 (smallest value)
#print(a)
print(heapq.heappushpop(a,28))
print(a)

print(heapq.heapreplace(a,3))
print(a)

#With other data structures:
class DataWrap:
    
    def __init__(self, data):
        self.data = data  
    
    def __lt__(self, other):
        return len(self.data) < len(other.data) #operator overloading function for comparison operators, contains the logic to compare the lengths of strings. 
# Create list of strings
my_strings = ["write", "go", "run", "come"]
# Initialize the sorted list
sorted_strings = []
# Wrap strings and push to heap
for s in my_strings:
    heapObj = DataWrap(s)
    heapq.heappush(sorted_strings, heapObj)
# Print the heap
for myObj in sorted_strings:
    print(myObj.data, end="\t")