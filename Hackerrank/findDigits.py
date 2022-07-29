#d is a divisor of n (n%D == 0)
#GIVEN INT FOR EACH DIGIT THAT MAKES UP THE INTEGER, DETERMINE IF IT IS A DIVISOR 
#COUNT NUMBER OF DIVISORS WITHIN THE INTEGER, EACH DIGIT IS UNIQUE

def findDigits(n):
    count=0
    for i in str(n): #turn n into string to check condition
        if int(i)!= 0 and n%int(i)==0:
            count +=1
    return count
        