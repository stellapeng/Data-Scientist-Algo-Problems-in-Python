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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections = sorted(connections, key=lambda x: x[2])
        uf = UF(n+1)
        mst = 0
        for c in connections:
            p1 = c[0]
            p2 = c[1]
            weight = c[2]
            
            if uf.connected(p1, p2):
                continue
            
            uf.union(p1, p2)
            mst += weight
        return mst if uf.count == 2 else -1 # 0 is used, it takes one count
            