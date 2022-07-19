#video game: character jumps height of k, with potion, it can jump k+1, given an array of heights,
#calculate how many potions character needs to take to clear all hurdles
#need to calculate difference between jumping ability and heights in array. Use a counter = h - k to
#determine amount of times character needs potion
def hurdleRace(k, height):
    count = 0
    for h in height:
        if h > k:
            count += h-k 
            k=h
    return count