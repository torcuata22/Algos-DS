#Utopian Tree: tree has 3 cycles of growth a year. IN spring, it doubles its height (from h to 2*h)
#in Summer, h=h+1. After n growing cycles, calculate a sapling's height

def utopianTree(n):
    height=1
    for growthCycle in range (1, n+1):
        if growthCycle%2==0:
            height *=2
        else:
            height +=1
    return height