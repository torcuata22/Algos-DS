#f(x)  that inverts order of words from first to last to last to first
#s=string to be inverted, start=0, end=last index (len(s)-1)

def reverseString(s, start, end):
    start,end = 0, len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start] #assign start to last and end to first (reversing string)
        start, end = start+1, end-1
 #time complexity: O(n), memory: O(1)    
        
#test:
s = "I don't like this very much"
#convert string to list to use iit as characters array
s=list(s)
start = 0
while True:
    try:
        end = s.index('',start)
        reverseString(s, start, end-1)
        start = end+1
    except ValueError:
        reverseString(s, start, len(s)-1)
        break
        
 
#Using a Stack: takes more space than the previous one: O(n)  
def reverseString(self, s:list[int]) ->None:
    stack = []
    for c in s:
         stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i +=1
     
             
#LEETCODE:

#Method 1: Slice notation

def reverse_String(s):
    n = len(s)-1
    return s[n::-1]

#Method 2: .join
def one_line_reverse(s):
    return " ".join(reversed(s)) #reversed is a built-in function, and wrap "join" around it
 
#Method 3: For Loop
def reverseLoop(s):
   result=''
   for i in s: #loop over every character 
       result = i + result #prepend i to result so we invert (because it goes from 1-n, but with prepend will return n-1)
   return result 