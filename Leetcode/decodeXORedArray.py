#see notes for definition of XOR (^)
#we are given encoded= (encoded version of arr) it is array of integers and first=integer (first in array we're looking for)
#find arr = array before encoding

def decode(encoded, first):
    arr=[first]
    for element in encoded:
        arr.append(arr[-1]^element)
    print (arr)
    
enco = [6,2,7,3]
decode(enco,4)