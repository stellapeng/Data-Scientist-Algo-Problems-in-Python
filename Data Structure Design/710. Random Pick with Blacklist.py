# use dictionary to map the gaps (elements on the blacklist)

# Time Complexity: O(b) preprocessing, O(1) pick
# Space Complexity: O(B)

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = blacklist
        self.size = n - len(blacklist)
        self.last_element = n - 1
        self.mapBlacklist = {}

        for b in self.blacklist:
            self.mapBlacklist[b] = -1

        for b in self.blacklist:
            if b >= self.size:
                continue
            while (self.last_element in self.mapBlacklist):
                self.last_element -= 1

            self.mapBlacklist[b] = self.last_element
            self.last_element -= 1
                

    def pick(self) -> int:
        
        rd = randrange(self.size)
        if rd in self.mapBlacklist:
            return self.mapBlacklist[rd]
        else:
            return rd
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()