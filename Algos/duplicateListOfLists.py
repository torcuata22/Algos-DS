#To remove duplicate from a list of lists:
#This approach requires that the lists are identical (order of elements, not just the elements), otherwise it won't consider it a duplicate

my_list = [[1,2,3], [1,2], [2,3], [1,2,3], [2,3], [1,2,3,4]]

def remove_dupe_list_of_lists(the_list):
    unique = []
    for sublist in the_list:
        if sublist not in unique:
            unique.append(sublist)
            
    print(unique)
remove_dupe_list_of_lists(my_list)
