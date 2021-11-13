from collections import deque

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = {i: [] for i in range(self.vertices)}
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def BFS(self, u):
        visited = [False for i in range(self.vertices + 1)]
        distance = [-1 for i in range(self.vertices + 1)]

        distance[u] = 0
        queue = deque()
        queue.append(u)

        visited[u] = True

        while queue:

            first = queue.popleft()

            for i in self.adj[first]:
                if not visited[i]:
                    visited[i] = True
                    distance[i] = distance[first] + 1
                    queue.append(i)
        
        maxDis = 0

        for i in range(self.vertices):
            if distance[i] > maxDis:
                maxDis = distance[i]
                nodeIdx = 1

        return nodeIdx, maxDis
    
    def LogestPathLength(self):
        node, Dis = self.BFS(0)
        node_2, LongDis = self.BFS(node)
        print('Longest path is from', node, 'to', node_2, 'of length', LongDis)


