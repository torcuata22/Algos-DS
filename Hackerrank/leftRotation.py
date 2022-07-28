def rotLeft(a,d):
    rot_list = a[d:] + a [:d]
    #return rot_list
    print (rot_list)

a = [1,2,3,4,5]
rotLeft(a,3)