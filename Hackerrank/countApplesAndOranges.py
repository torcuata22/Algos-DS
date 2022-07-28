#given distance from trees to house, count how many oranges and apples fall on house
#Apples, Oranges are arrays. If elements of arrays are within the interval of s and t, the fruit fell on the house
#I need to add distances plus position and compare to interval, count how many elements in each array fall in interval

def countApplesAndOranges(s,t,a,b,apples,oranges):
    count_apples = 0
    count_oranges = 0
    #count for as long as I have elements in array:
    for i in range(len(apples)):
        if a+apples[i] >=s and a+apples[i] <=t:
            count_apples +=1
    for i in range(len(oranges)):
        if b+oranges[i] >=s and b+oranges[i] <=t:
            count_oranges +=1
    print(count_apples)
    print(count_oranges)       