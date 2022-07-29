#f(x)  that inverts order of words from first to last to last to first
#s=string to be inverted, start=0, end=last index (len(s)-1)

def reverseString(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start] #assign start to last and end to first (reversing string)
        start = start+1
        end -=1
        
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
        