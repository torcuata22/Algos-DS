#Implement a queue using Stack (completely counter intuitive)

from collections import deque

class Stack:
    def __init__(self):
        self.q = deque
        
    def push(self, data):
        s= len(self.q)
        self.q.append(data) #push the current element
        for i in range (s): #pop all previous elements and put them after current element
            