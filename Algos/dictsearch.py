def linear_search_dictionary (my_dict, target):
    for key in my_dict:
        if my_dict[key] == target:
            print("Target found at key: ", key)
            return key
    
    print("Target not found, please try a new target")
    

my_dictionary = {"red": 5, "blue": 3,  "yellow": 12, "green": 7}

linear_search_dictionary(my_dictionary, 27)



