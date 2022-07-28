#Professor cancels class if there are fewer than k number of students present at time class starts.
#If t (time of arrival) =< 0, students count towards k, if t>0, students don't count
#a is a list with arrival times

def angryProfessor(k,a):
    count=0
    for t in a:
        if t <= 0: #students who are early or on time
            count +=1
        
    if count < k: #class is cancelled
        print ("YES")
    else: #class not cancelled
        print("NO")