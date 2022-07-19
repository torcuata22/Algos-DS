#Two cats after one mouse, determine which cat gets to mouse first if both cats run at same speed from different
#positions. If cats get to mouse at the same time (same difference in distance), mouse wins

def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB=abs(y-z)
    if catA == catB:
        return "Mouse C"
    elif catA < catB:
        return "Cat A"
    else:
        return "Cat B"