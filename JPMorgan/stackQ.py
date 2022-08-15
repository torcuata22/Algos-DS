#Implement a queue using Stack (completely counter intuitive)

from collections import deque

class Stack:
    def __init__(self):
        self.q = deque
        
    def push(self, data):
        s= len(self.q)
        self.q.append(data) #push the current element
        for i in range (s): #pop all previous elements and put them after current element: first we pop, then we append
            self.q.append(self.q.popleft())
    
    #we need to remove the top element because queues are FIFO and stacks are LIFO
    def pop(self):
        if not self.q:
            print("No elements")
        else:
            self.q.popleft()
            
    #finally we need to return the top of the stack
    def top(self):
        if not self.q:
            return
        return self.q[0]
    
    #driver code:
    if __name__ == '__main__':
        st = Stack()
    st.push(40)
    st.push(50)
    st.push(70)
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())
    st.push(80)
    st.push(90)
    st.push(100)
    print(st.top())
    st.pop()
    print(st.top())
    st.pop()
    print(st.top())