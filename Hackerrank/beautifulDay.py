#beautifulNumber is defined as a number i that: abs(i-reverse(i))% = 0
#Given range of numbers [i,...,j], calculate number of beautiful days
#Will need two functions: one to reverse the number and  determine if it's beautiful or
#not and another to count the number of beautiful days

def is_beautiful(num,k):
    reverse=int(str(num)[::-1]) #[::-1] reverses the string, then we convert back to int so we can operate
    return abs(num-reverse)%k == 0 
        
def beautifulDay(num,k):
    result = 0
    if is_beautiful(num,k):
        result +=1
    return result