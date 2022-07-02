#Using recursion:
def reversePrint(head):
    if head == None: #empty LList
        return
    reversePrint(head.next) #Traverse to the end and then starts travelling back
    print(head.data)
    
#Using list slicing:

