class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None #keeps track of the stack's head
        self.num_nodes = 0 #keeps track of the number of nodes in the stack at all times

    def push(self, value):
        new_node = Node(value) #instantiate node from node class to hold value that will be pased in

        if self.head is not None:
            new_node.next = self.head  
            
        self.head = new_node
        self.num_nodes += 1

    def pop(self): #the value being popped off the list is used as the return value, so I don't need a value parameter
        if self.head == None: #checks if there are no items in the stack, lets the method know there was nohthing to pop
            return None

        pop_node = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return pop_node #lets the caller of the method know that this was the value that was popped


stack = Stack() #this instantiates a class object from the class
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.num_nodes == 5) else "Fail")
print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
