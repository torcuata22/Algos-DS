#ad shown to p number of people, assume floor(p/2) people like it and show it to +=3 people
#The next day, the number of people changes to: 3*floor(p/2), and so on each day. If the original p=5
# how many people liked the ad after n days? (launch day=1 => list is indexed at 1 not 0!)

def viralAd(n):
    num_people = 5 #initial number of people
    likes = 0
    total_likes=0 
    for day in range (n):
        likes = num_people//2
        total_likes+=likes
        num_people = 3*likes