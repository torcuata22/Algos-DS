#Given array "points" representing integer coordinates of some points on a 2D plane, where
#points[i] = [xi,yi]. The cost of connecting two points (xi,yi) and (xj,yj) is abs(xi=xj) + abs(yi-yj)
#Return minimum cost to make all points connected (points are connected if exactly ONE simple path between 2 points)
#Minimum Spanning Tree (minimum cost to connect al points): Prim's algorithm
#Edges = distance between points (Manhattan distance)
#Steps:BEFORE IMPLEMENTING PRIM: Determine N (number of nodes) = len(points); create adjacency list: 
#adj = {i:[] for i in range(N)} where i is index, right now it's  of empty list which we will build it using i
#list = [cost, node] for each edge, weight of edge = distance from one node to the next, we are looking for min distance
#j = i+1, meaning they are adjacent to each other

#This first half creates adjacency list and calculates distances(weights)
import heapq


class Solution:
    def minCostConnectPoints(self, points:list[list[int]])->int:
        N = len(points)
        adj = {i:[] for i in range(N) }
        j=i+1
        for i in range(N):
            x1,y1 = points[i]
            for i in range(j, N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append[dist,j]
                adj[j].append[dist, i]
                
#Second half: Implementing Prim's algorithm (stay inside function!):
#IMPORTANT: minH= [cost,point], cost MUST come first b/c this is what minHeap will pop
        res = 0
        visit = set()
        minH = [[0,0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH) #pop min. value
            if i in visit: #verifies that we haven't visited that node, if we have, skip it
                continue
            res+= cost #add cost of the node to res (result)
            visit.add(i) #if i wasn't in visit, we add it now so we don't repeat
            for neiCost, nei in adj[i]: #neiCos, nei are neighbor cost and neighbor number respectively
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res

        
        
        