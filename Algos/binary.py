#Binary search algorithm:

def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:  #list is not empty
        pivot = (lower_bound + upper_bound) // 2 # pivot is half-way between upper and lower bounds
        pivot_value = the_list[pivot] 
 

        if pivot_value == target:  # search over
            return pivot

        if pivot_value > target:  # in this case, we discard upper half of the list
            upper_bound = pivot - 1  # upper bound is one below pivot, which discards the upper half

        else:  # pivot lower than target, in which case, we can get rid of lower half
            lower_bound = pivot + 1  # lower bound is one above pivot now, so we discard lower half

    return -1  # means target value was not found


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 10))
print(binary_search(my_list, 4))
print(binary_search(my_list, 33))