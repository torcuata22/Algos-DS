#Huffman coding assigns variable length codewords to fixed length input characters based on frequency
#more frequent characters have longer codewords
#Every leaf is a character with its frequency count
#Letters are assigned sequences of ones and zeroes that make up the path down the tree to reach the letter from the root
#zeroes mean left side of the tree (root.left) and ones mean right side (root.right)

def huffman(root,s):
    #store root in temporary variable I'll use to traverse the tree and result is an empty list where I'll store letters
    temp = root
    result = []
    #use for loop to traverse binary coded string (for every character in the string s)
    for char in s:
        if char == 0:
             temp = temp.left
        else:
            temp = temp.right
        #I need to check for a leaf node:
        if temp.left == None and temp.right == None:
            result.append(temp.data)
            temp = root
            #after appending leaf (letter) to result, we return to the root (temp = root) to traverse again
            
    print(''.join(result)) #turns list into string)