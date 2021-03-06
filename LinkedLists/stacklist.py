class Stack:
    def __init__(self):
        self.items=[] #this is an empty list, this sets up the class to use python list and its methods
        
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.size == 0:
            return None
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    #apend(), push() and pop() are list methods, as well as the len() function
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.size() == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
    