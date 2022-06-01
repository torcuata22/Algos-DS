unsorted_list = [101, 49, 3, 12, 56]

def bubble_sort(the_list):
    high_idx = len(the_list)-1
    for i in range(high_idx):
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]
            
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                
    print(the_list, i, j)
    
bubble_sort(unsorted_list)

#added list_changed flag to track if list changes with any i loop iteration
def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_changed = False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True

            print(the_list, i, j)
        print(list_changed)
        if list_changed == False:
            break