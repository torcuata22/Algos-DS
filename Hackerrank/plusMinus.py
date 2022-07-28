def plusMinus(arr):
    x,z,y=0,0,0
    for i in range(0,len(arr)):
        if arr[i]>0:
            x = x + 1
        elif arr[i]<0:
            y = y + 1
        else:
            z = z + 1
    print('%.6f'%(x/len(arr)))
    print('%.6f'%(y/len(arr)))
    print('%.6f'%(z/len(arr)))
    

test = [-4,3,-9,0,4,1]
plusMinus(test)