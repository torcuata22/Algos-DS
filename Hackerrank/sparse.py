def matchingStrings(strings, queries):
    results=[]
    for q in queries:
        arr= [x for x in strings if x == q]
        results.append(len(arr))
    return results