# Time complexisity: O(∣E∣+∣V∣^2)
# Space complexisity: O(∣E∣+∣V∣)

class Solution:
    def __init__(self):
        self.has_cycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for pair in prerequisites:
            course, preq = pair[0], pair[1]
            graph[course].append(preq)
        
        colour = ['white'] * numCourses # initialize outside the for loop
        for i in range(numCourses):  
            self.traverse(graph, i, colour)
            if self.has_cycle:
                return False
        
        return True
        
    def traverse(self, graph, vertex, colour):     

        if self.has_cycle:
            return
        
        colour[vertex] = 'grey' # encountered

        for v in graph[vertex]:
            if colour[v] == 'grey':
                self.has_cycle = True
            if colour[v] == 'white':
                self.traverse(graph, v, colour)

        colour[vertex] = 'black' # explored



class Solution:
    def __init__(self):
        self.has_cycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for pair in prerequisites:
            course, preq = pair[0], pair[1]
            graph[course].append(preq)
        
        on_path = [False] * numCourses # initialize outside the for loop
        visited = [False] * numCourses # initialize outside the for loop
        for i in range(numCourses):
            self.traverse(graph, i, on_path, visited)
            if self.has_cycle:
                return False
        
        return True
        
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
        on_path[vertex] = False

            

