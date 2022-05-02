# Time Complexisity: union and find are O(1)

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if (rootP == rootQ):
            return
        
        self.parent[rootQ] = rootP
        self.count -= 1
        
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def find(self, x):
        while (self.parent[x] != x):
            # compress the depth
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for e in edges:
            uf.union(e[0], e[1])
        return uf.count
            
        