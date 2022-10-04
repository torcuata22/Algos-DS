#compress string s. When a character is repeated  k times consecutively (ex: aaa), the encoded form would be characterk 
#(ex: aaa would become a3). No need to count single characters
#Ex. input = abbaaaaaccaaab, then the output would be: ab2a5c2a3b

def compress(s):
    res = ''
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            res = res + s[i-1]
            if count > 1:
                res += str(count)
            count =1
    res = res + s[-1]
    if count > 1:
        res+=str(count)
    print(res)
    
s='abbaaaaaccaaab'
compress(s)
        
            