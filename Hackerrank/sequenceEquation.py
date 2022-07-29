#Given a sequence of integers p= p(1), p(2), ...,p(n) where all p(x) are different
#from each other and 1,+ x <= n, find an integer so that p(p(x))=x
#Keep history of y = p(x) and return as array
#p=[list where 1<= p[i] <= len(p)]
#iterate from 1 to len(p)+1 using i as counter and store index of i in new list (indices)
#iterate the elements and store index of elements in the answer

def permutationEquation(p):
    indices=[]
    for i in range(1,len(p)+1):
        indices.append(p.index(i)+1) #index() is a built-in function that searches for element in a list and returns lowest index said element appears
        
    ans=[]
    for element in indices:
        ans.append(p.index(element)+1)
    return ans