#Given an array representing bird sightings (numbers = id of birds), determine the id of most frequently sighted
#If more than one id, return the lowest id value

def migratoryBirds(arr):
    l=[0] * len(arr)
    for i in range (len(arr)):
        l[arr[i]] +=1
    return l.index(max(l))
