#GIVEN TO INTEGER ARRAYS, FIND NUMBER THAT SATISFIES BOTH OF THESE:
#EVERY ELEMENT OF ARRAY 1 ARE FACTORS OF THE NUMBER
# THE NUMBER IS A FACTOR OF ALL THE ELEMENTS OF SECOND ARRAY   
#Calculate Greater Common Denominator and Lower Common Multiple (gcd and lcm), to do this import reduce frmo functools

from functools import reduce
def getTotalX(a,b):
    def gcd(a,b):
       if b == 0:
           return a
       return gcd(b, a%b)
    def lcm(a,b):
        return a * b // gcd(a,b)
    l = reduce(lcm, a)
    g = reduce(gcd, b)
    s = 0
    
    for i in range (l, g+1, l):
        if g%i == 0:
            s +=1
    return s
    
             