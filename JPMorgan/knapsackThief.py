#Thief wants to steal items for maximum profit,  but sack has limited capacity. Create algorithm
#to ensure maximum profit
#Case One: number of items(n) or capacity of bag == 0, return 0
#Case two: weight of the item is > than capacity, then ignore the item
#case three: weight of item < capacity, so grab item


#THIS DOESN'T WORK
def knapsack(capacity:int, weights:list, profits:list, n:int):
   
        if n ==0 or capacity ==0:
            print(0) 
        
        if weights[n-1] > capacity:
            print(knapsack(capacity, weights, profits, n-1))
        
        else:
            print (max(profits[n-1] + knapsack(capacity-weights[n-1], weights, profits, n-1), knapsack(capacity, weights, profits, n-1))) 
   

profits=[24,18,18,10]
weights=[24,10,10,7]
capacity=25
n=len(weights)
knapsack(capacity,weights,profits,n)