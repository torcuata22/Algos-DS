def dynamicArray(n, queries):
    col = [[] for i in range(n)]
    res = []
    lastanswer = 0
    for q in queries:
        data = (q[1]^lastanswer)%n
        if q[0] == 1:
            col[data].append(q[2])
        elif q[0] == 2:
            ind_x = q[2]%len(col[data])
            lastanswer = col[data][ind_x]
            res.append(lastanswer)
    return res 

#found on Stack Overflow!