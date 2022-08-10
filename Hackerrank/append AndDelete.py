#append lower case letter to the end of a string, delete lat character of said string. Given an integer k,
#and two strings: s and t, determine if you can convert s into t in k or fewer moves. If it is possible
#return Yes, if not return No.
#Use zip(a,b) where a, b are both iterator objects that will be joined together. Use it
# to compare strings. zip() returns tuples:((a1,b1), (a2,b2),...(an,bn)). If there are any "leftovers"
#because a and b have different lengths, the leftovers are ignored.
#We have to satisfy three cases: First, t_len <=2*count+k, in which case, AND at the same time, Second: t_len % 2 == k%2, 
# the third case: t_len < k, would leave us with no restrictions because we the sum of the length of 
#both strings is smaller than k. Conditions to satisfy: First and second or third


def appendAndDelete(t,s,k):
    count = 0
    #calculate how many matching characters in strings
    for i, j in zip(s,t):
        if i == j:
            count +=1
        else:
            break
    t_len=len(s) + len(t) #this is the total length of the two strings
    if t_len <= 2*count+k and t_len%2 == k%2 or t_len <k:
        return "Yes"
    else:
        return "No"
    
        