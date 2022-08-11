#given two strings, check if they're anagrams.
#First: convert to all lower case and check if they're the same length
#Second: Sort both strings
#Third: compare strings to see if they're equal

from audioop import ratecv


def checkAnagram(s1:str, s2:str):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        sorted1=sorted(s1)
        sorted2=sorted(s2)
        if sorted1 == sorted2:
            print("The strings are anagrams of each other" )
        else:
            print("the strings are not anagrams")
    else:
        print("the strings are not anagrams")
        
        
s1='rsCe' 
s2='CAremmrr'
checkAnagram(s1,s2)
        