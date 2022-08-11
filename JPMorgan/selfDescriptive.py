#self-descriptive number: when a digit in position N-1 is same as its index
#write function to determine if number is self-descriptive or not
#start by converting number int a string
#iterate for the length of s, placing number in temp variable and using ord() and count
#how many times the number repeats itself
#b stores the digit present on index i, count is how many times digit is repeated throughout string

def selfDescriptive(num):
    s = str(num)
    for i in range(len(s)):
        temp = s[i]
        b=ord(temp)-ord('0')
        count=0
        for j in range(len(s)):
            temp2=ord(s[j])-ord('0')
            if temp2 == i:
                count+=1
        if count!= b:
            return False
    return True
