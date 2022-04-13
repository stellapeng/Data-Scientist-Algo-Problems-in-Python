# traverse DFS

# Time Complexisity: O(V+E)
# Space Complexisity: O(V+E)


class Solution:
    def __init__(self):
        self.visited = []
        self.colour = []
        self.res = True
        
    def traverse(self, graph, vertex):

        self.visited[vertex] = True
        
        for v in graph[vertex]:
            if self.visited[v] == False:
                self.colour[v] = -self.colour[vertex]
                self.traverse(graph, v)
            elif self.colour[v] == self.colour[vertex]:
                self.res = False
                break
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.visited = [False] * len(graph)
        self.colour = [1] * len(graph)
        
        for i in range(len(graph)):
            if self.visited[i] == False:
                self.traverse(graph, i)
                
        return self.res
        