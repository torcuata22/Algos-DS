#given network of n nodes, labeled from 1 to n, also given times, a list of travel times as directed edges:
#times[i] = (ui,vi,wi), where ui is the source node and wi = time it takes signal to travel source to target
#we will send signal from node k. Return time it takes for all the n nodes to receive the signal
#If it is impossible for all the n nodes to receive signal, return -1

import collections
import heapq
import sys


def networkDelayTime(self, times:list[list[int]], n:int, k:int) -> int:
    edges = collections.defaultdict(list)
    for u,v,w in times:
        edges[u].append((v,w))
    minHeap = [(0,k)]
    visit = set()
    t=0
    while minHeap:
        w1,n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t=max(t,w1)
        
        #breadth search portion of the algo:
        for n2,w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1+w2,n2))
    return t if len(visit) == n else -1

#Geeks for Geeks solution:
class Graph():
     
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)