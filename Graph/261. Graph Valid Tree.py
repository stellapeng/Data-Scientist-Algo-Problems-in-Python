# Kruskal

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i
        
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        
        if root_p == root_q:
            return
        self.parent[root_p] = root_q
        self.count -= 1
    
    def find(self, p):
        while (p!= self.parent[p]):
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        return root_p == root_q
        
class Solution:        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for e in edges:
            p1 = e[0]
            p2 = e[1]
            if uf.connected(p1, p2):
                return False
            uf.union(p1, p2)
        
        return uf.count == 1
        