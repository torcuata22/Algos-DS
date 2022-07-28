#Form a magic square: n*n matrix of ints from 1 to n**2 where sum rows, sum cols, sum diagonals = constant
#(the magic constant)
import sys

def formingMagicSquare(s):
    magic =  [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], 
              [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], 
              [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    minimumcost = sys.maxsize
    for item in magic:
        diff = 0
        for i, j in zip(s,item):
            diff += abs(i-j)
            minimumcost=min(minimumcost, diff)
    return min(minimumcost, diff)
#DOESN'T WORK