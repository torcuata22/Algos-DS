#Write efficient program to count the number of 1s in the binary representation of an integer

#Method 1: loop through all bits, set if bit is set and it if is count=+1
def countBits(n):
    count = 0
    while (n):
        count +=n & 1
        n>>=1
    return count


#Recursive approach:
def count_bits(n):
    if n==0:
        return 0
    else:
        return(n & 1) + count_bits(n>>1)
    
#Leetcode:
def count_bits2(n):
    ans = 0
    while n:
        n &= (n-1) #n&=(n-1) removes rightmost binary representation of n
        ans +=1
    return ans

