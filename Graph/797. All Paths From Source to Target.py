class Solution:
    def __init__(self):
        self.res = []
        
    def traverse(self, graph, s, l, path):
        path.append(s)
        
        if s == l - 1:
            # pass by reference, need to deep copy the path list before adding to result
            path_copy = [i for i in path] # or path.copy()
            self.res.append(path_copy)
            print(path)
            path.pop()
            return
        
        for adjescent in graph[s]:
            self.traverse(graph, adjescent, l, path)
            
        path.pop()
            
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = len(graph)
        path = []
        self.traverse(graph, 0, l, path)
        return self.res



# the pseudo code of traversing a graph:
colour = []

def traverse(graph, vertex):
    colour[vertex] = 'grey' # vertex is encountered

    for adj of vertex:
        if colour[adj] == 'white'
        traverse(graph, adj)

    colour[vertex] = 'black' # vertex is explored