# traverse DFS

# Time Complexisity: O(V+E)
# Space Complexisity: O(V+E)


class Solution:
    def __init__(self):
        self.visited = []
        self.colour = []
        self.res = True
        
    def traverse(self, graph, vertex):
        if(not self.res):
            return
            
        self.visited[vertex] = True
        
        for v in graph[vertex]:
            if self.visited[v] == False:
                self.colour[v] = -1 * self.colour[vertex]
                self.traverse(graph, v)
            elif  self.colour[v] == self.colour[vertex]:
                print(v, vertex)
                self.res = False

                
    def buildGraph(self, n, dislikes):
        graph = defaultdict(list)
        for i in range(1, n+1):
            graph[i] = []
        for pair in dislikes:
            p1, p2 = pair[0], pair[1]
            graph[p1].append(p2)
            graph[p2].append(p1)
        return graph
                
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.visited = [False] * (n+1)
        self.colour = [1] * (n+1)
        
        graph = self.buildGraph(n, dislikes)
        print(graph)
        for i in range(1, n+1):
            if not self.visited[i]:
                self.traverse(graph, i)
                
        return self.res