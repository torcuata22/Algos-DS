def bonAppetit(bill, k, b): 
    s = sum(bill)
    charges = (s-bill[k])//2
    
    if b == charges:
        print ("Bon Apetit")
    else:
        print(b-charges)