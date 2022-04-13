# topological order:
# 1) traverse DFS
# 2) reverese the explored nodes

# Time Complexisity: O(V+E)
# Space Complexisity: O(V+E)

class Solution:
    def __init__(self):
        self.has_cycle = False
        self.order = []
        
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for pair in prerequisites:
            course, preq = pair[0], pair[1]
            graph[preq].append(course)
            
        
        on_path = [False] * numCourses # initialize outside the for loop
        visited = [False] * numCourses # initialize outside the for loop
        order = []
        for i in range(numCourses):
            self.traverse(graph, i, on_path, visited)
            if self.has_cycle:
                return []
        ans = self.order
        return ans[::-1]
        
    def traverse(self, graph, vertex, on_path, visited):     
        if on_path[vertex]:
            self.has_cycle = True
            return
        
        if visited[vertex]:
            return
        
        # pre-order
        on_path[vertex] = True
        visited[vertex] = True
        
        for v in graph[vertex]:
            self.traverse(graph, v, on_path, visited)
    
        # post-order
        self.order.append(vertex)
        on_path[vertex] = False

            

