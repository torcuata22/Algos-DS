#Given a number of socks, n, and an array of colors, calculate number of pairs
def sockMerchant(n,ar):
    count = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            count += 1 
            color.remove(ar[i])
    return count
