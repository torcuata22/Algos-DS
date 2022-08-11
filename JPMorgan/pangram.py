#find missing letters to create a pangram (a sentence containing every letter in the English alphabet)
#create Bool array (all False, then change values accordingly, print False values)

from string import punctuation, ascii_lowercase
from collections import defaultdict

#Method1: use ord() to determine index of missing letter (ord() returns unicode value of letter)
def missingChars(my_string):
    Max_Char = 26
    present = [False for i in range(Max_Char)]

    #figure out indeces in present that have letters in the given string:
    for i in range(len(my_string)):
        if my_string[i] >='a' and my_string[i] <='z':
            present[ord(my_string[i])-ord('a')] = True
        elif my_string[i] >='A' and my_string[i] <='Z':
            present[ord(my_string[i])-ord('A')] = True

    res = ''
    for i in range(Max_Char):
        if present[i] == False:
            res += chr(i+ord('a'))
           
            
    #return res
    print (res)
    
#Method 2: using ascii_lowercase, punctuation from string and defaultdict from collections:
#lookup string alphabet, remove chars from it if its present in the input string, then
#print remaining letters from the alphabet lookup string


def isPanagram(sentence):
    sentence = sentence.lower()
    letterCount = defaultdict(int)
    for letter in ascii_lowercase:
        letterCount[letter] = 0
    for letter in sentence:
        if letter in punctuation:
            continue # Skip special characters / punctuation marks
        letterCount[letter] += 1

    missingLetters = [letter for letter, count in letterCount.items() if count == 0]
    if len(missingLetters) == 0:
        print('The sentence is a panagram!')
    else:
        print('The sentence is not a panagram and is missing the letters: ', missingLetters)
    
s= 'the fox jumped over the fence'
#missingChars(s)
isPanagram(s)
    