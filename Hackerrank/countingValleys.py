#hiker counts how many steps in a valley and how many on mountain while hiking U=uphill
#D=downhill steps. Steps is the number of steps, path is a string describing the terrain

def countingValleys(steps, path):
    valleys = 0
    cur_level = 0
    for steps in path:
        if(steps == 'U'):
            cur_level += 1
            if(cur_level == 0):
                valleys += 1
        elif(steps == 'D'):
            cur_level -= 1
    return(valleys)
