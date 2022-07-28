#determine area of rectangle made up by letters in a word (assume all letters are 1mm wide)
#you are given a list of all letter heights and a string (word), so need to iterate through 
# letters in the string, find the height, pick tallest letter, and calculate the area. 
# Total width = len(list), area = max height * total width

def designerPdfViewer(h, word):
    height = 0
    for letter in word:
        height = max(height, h[ord(letter)-ord('a')])
    return height * len(word)



