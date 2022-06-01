#BASIC LINEAR SEARCH ALGORITHM

def linear_search(the_list, target):
    for x in range(len(the_list)): #we are searching by index,not item value
        if the_list[x] == target:
            print ("Target found at index ", x)
            return x
    print ("Target not on the list")
    return -1
my_list = [6,3,7,9,1,0,33]  
linear_search(my_list, 7)  
   

        