#Works, but Hackerrank wouldn't accept it:
# def staircase(n):
#     for i in range (0,n): Maybe it's because of the ZERO, it should be 1
#         s = n-i-1
#         hash=i+1
#         print(s*" ",hash* "#")
        
    
#It accepts this:      
def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)
        
        
staircase (10)