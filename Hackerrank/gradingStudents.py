#Conditions:#
#grade < 40 = Fail
#if grade%5 < 3, round up to next multiple of 5
#if grade <38, no rounding up

def gradingStudents(grades):
    for i in range(0,len(grades)):
        if grades[i] < 38:
            continue
        else:
            temp = grades[i]
            mod5 = temp % 5
            if mod5 == 3:
                temp = temp + 2
                grades[i] = temp
            elif mod5 == 4:
                temp = temp + 1
                grades[i] = temp
            else:
                continue
    return grades
