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
    
#GEEKS FOR GEEKS PRIM:
# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# A utility function to print the constructed MST stored in parent[]
	def printMST(self, parent):
		print ("Edge \tWeight")
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][parent[i]])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minKey(self, key, mstSet):

		# Initialize min value
		min = sys.maxsize

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	# Function to construct and print MST for a graph
	# represented using adjacency matrix representation
	def primMST(self):

		# Key values used to pick minimum weight edge in cut
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		# Make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 # First node is always the root of

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# Put the minimum distance vertex in
			# the shortest path tree
			mstSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m
				# mstSet[v] is false for vertices not yet included in MST
				# Update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u

		self.printMST(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]

g.primMST();





        
        
        