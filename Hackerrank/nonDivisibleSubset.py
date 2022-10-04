#See hackerrank description of problem 

def nonDivisibleSubset(k, s):
    rem = [0]*k
    for i in s:
        rem [i%k] +=1
        
    maxnum = 0
    maxnum += min(rem[0],1)
    if k%2 == 0:
        maxnum += min(rem[k//2],1)
    for i in range (1, k//2 +1):
        if i != k-i:
            maxnum +=max(rem[i], rem[k-i])
    return maxnum
