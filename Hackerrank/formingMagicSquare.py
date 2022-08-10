#Form a magic square: n*n matrix of ints from 1 to n**2 where sum rows, sum cols, sum diagonals = constant
#(the magic constant)
import sys
#import numpy as np (must install first)

pre =  [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], 
              [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], 
              [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]


def formingMagicSquare(s): 
    results = []
    for p in pre:
        total = 0
        for p_row, s_row in zip(p, s):
            for i, j in zip(p_row, s_row):
                if not i == j:
                    total += max([i, j]) - min([i, j])
            
        results.append(total)
        
    return min(results)

# Create an N x N magic square using numpy. N must be odd.

'''
N  = 5
magic_square = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

print(magic_square)

'''