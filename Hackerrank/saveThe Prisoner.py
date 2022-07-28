#p=number of prisoners, t=number of treats. Divide treats by sitting p in circular table with 
#numbered chairs. Start at random number. Distribute candy sequentially until t=0
#One bad candy. Determine chair number who will receive the bad candy
#n=number of prisoners, m=number of sweets, s=initial chair number
#return: warn=chair number to warn
#warn=(s+m-1)%n
#if warn=0, the prisoner to warn is n

def savePrisoner(n,m,s):
    warn=(s+m-1)%n
    if warn == 0:
        return n
    return warn