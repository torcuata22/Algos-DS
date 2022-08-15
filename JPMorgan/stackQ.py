#Implement a queue using Stack (completely counter intuitive). Use two queues

from collections import deque

class Stack:
    def __init__(self):
       self.q1 = deque()
       self.q2 = deque() 
       
    def push(self, x):
        self.q1.append(x)
        
    def pop(self):
        #if q1 is empty:
        if not self.q1:
            return
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft()) #append popped items form q1 to q2, leaving 1 element in q1 (that's why len(q1)==1)
            top=self.q1[0]
            self.q2.append(self.q1.popleft()) #we are popping the only element in q1 and appending it to q2)
            
            #swap the names of the queues:
            self.q1, self.q2 = self.q2, self.q1
            return top
        
        def size(self):
            return len(self.q1)
# 
 
    

  
            
            
            