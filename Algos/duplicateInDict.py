#To remove duplicate values from a list of dictionaries, we can use a loop
items = [{'name':'Nikki'},{'name':'Kate'}, {'name':'James'}, {'name':'Nikki'}, {'name':'Kate'}, {'name':'Mike'}]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print (unique)