from collections import Counter

#find (and return) duplicate values in list
#list comprehension to include item that is in the list more than once
#convert list to set to remove duplicates from filtered list, then converted back to list list(set()) part

the_list= ['a', 'b', 'a', 'd', 'm', 'a', 'f', 'c']
def find_dupes(my_list):
    dupes=[element for element in my_list if my_list.count(element)>1]
    unique_dupes=list(set(dupes))
    print(unique_dupes)


#To count how many times the item is repeated:
#Import Counter class from collections module
#Create Counter object with the list and convert it to a dictionary --> counts=dict(Counter(my_list))
#Filter the dictionary to remove any key:pair value where value is NOT >1
def count_dupes(my_list):
    counts = dict(Counter(my_list))
    dupes = {key:value for key, value in counts.items() if value >1}
    print (dupes)

#To remove duplicate in a list: use set() function
def unique_vals(my_list):
    unique = list(set(my_list))
    print(unique)
    
    
find_dupes(the_list)
count_dupes(the_list)
unique_vals(the_list)

