# use bottom up DP to memorize the interium results
# Time Complexisity: O(n^2)
# Space Complexisity: O(n)

class Solution:
    def __init__(self):
        self.memo = [[]]
        
    def count(self, low, high):
        # base case: null node counts as 1 case
        if low > high:
            return 1
        
        if self.memo[low][high] != -1:
            return self.memo[low][high]
        
        res = 0
        for i in range(low, high+1):
            left_cnt = self.count(low, i - 1)
            right_cnt = self.count(i + 1, high)
            res += (left_cnt * right_cnt) # the posibility is left * right
            
            self.memo[low][i-1] = left_cnt
            self.memo[i+1][high] = right_cnt
            
        return res
        
    def numTrees(self, n: int) -> int:
        # we dont want to bother with the -1 index
        # initilize the memo with (n+1) + 1
        self.memo = [[ -1 for i in range(n+2) ] for j in range(n+2) ]
        return self.count(1, n)

        