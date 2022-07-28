#Given an array representing bird sightings (numbers = id of birds), determine the id of most frequently sighted
#If more than one id, return the lowest id value

def migratoryBirds(arr):
    l=[0] * len(arr) #creates a list with len(arr) elements
    for i in range (len(arr)):
        l[arr[i]] +=1 #increment count for particular bird in index i
    return l.index(max(l)) #max(l) calculates max count, index returns index(type) of bird
