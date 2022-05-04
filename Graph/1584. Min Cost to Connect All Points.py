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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i, n):
                x1 = points[i][0]
                y1 = points[i][1]
                
                x2 = points[j][0]
                y2 = points[j][1]
                
                distance = abs(x1-x2)+abs(y1-y2)
                edges.append([i, j, distance])
        
        edges = sorted(edges, key=lambda x: x[2])
        uf = UF(n)
        mst = 0
        for e in edges:
            p1 = e[0]
            p2 = e[1]
            distance = e[2]
            if uf.connected(p1, p2):
                continue
            uf.union(p1, p2)
            mst += distance
        return mst
            
            
            
        