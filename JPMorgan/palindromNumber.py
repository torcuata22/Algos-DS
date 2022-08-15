#Write a program that takes number and gives the resulting palindrome (if one exists). 
# If it took more than 1, 000 iterations (additions) or yield a palindrome that is greater 
# than 4, 294, 967, 295, assume that no palindrome exist for the given number.
#start by reversing and adding digits, then check if it's  a palindrome (return) or not (continue)

def reverseNum(num:int)->int:
    rev = 0
    while num > 0:
        rev = rev * 10  + num %10
        num = num // 10
    return rev


def isPalindrome(num:int)->int:
    return (reverseNum(num) == num)

def reverseAndAdd(num:int)->int:
    rev = 0
    while num <= 4294967295:
        rev = reverseNum(num)
        num = num + rev
        
        if isPalindrome(num):
            print (num)
            break
        else:
            if num> 4294967295:
                print ("no palindrome exists")
        
        
        
    
        
        
        
reverseAndAdd(19)