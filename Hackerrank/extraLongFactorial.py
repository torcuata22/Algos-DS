#Calculate factorial of long integers (Python can handle long integers)
#n!=(n-1)*(n-2)*...*1

def extraLongFactorial(n):
    fact=1
    for i in range(1,n+1):
        fact*= i
    print (fact)