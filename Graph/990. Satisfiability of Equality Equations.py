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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UF(26)
        
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0]) - ord('a'), ord(e[3]) - ord('a'))
        for e in equations:
            if e[1] == '!':
                if uf.connected(ord(e[0]) - ord('a'), ord(e[3]) - ord('a')):
                    return False
        return True
        
        