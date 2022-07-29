#One rotation moves last array element to index=0 and shifts all the remaining ones. 
#a=array of ints (index = n)
#n=len(a)
#k=number of rotations (count)
#queries=list of indices to report (position, this is given to me)
#add queries (indices) to check in the array after performing k rotations
#starting_index=n-k (n=len(arr), k=number of rotations, k=query index)
#if n-k+q is greater than n-1, the index will be out of bounds. To prevent this we %n


def circularArrayRotation(a,k,queries):
    n=len(a)
    ans=[]
    idx=(n-k+q)%n #initial index of array a 
    for q in queries:
        ans.append(a[idx]) 
    return ans