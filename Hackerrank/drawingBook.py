#n=number of pages, p=page we want to go to.COunt number of page turns to get to p
#starting on page 1 and starting on last page (page n), return minimum of the two
#number of turned pages = n/2
def pageCount(n,p):
    front = p//2
    if n%2 == 1: #if it's odd
        back = (n-p)//2
    else: #if it's even
        back = (n-p+1)//2
    return min(front, back)