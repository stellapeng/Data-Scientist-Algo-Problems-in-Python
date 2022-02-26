''' 
what we are doing here is, in each iteration, we substract the 
by-far-minimul value from the current element, update the result if
it is larger.

dont use the built-in find min function which is O(n) in each call
we can do better - in each iteration, we only need one comparison to 
update or not the so-far-minimum.

Time complexity is O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        local_min = prices[0]
        for i in range(len(prices)):
            if prices[i] < local_min:
                local_min = prices[i]
            if prices[i] - local_min > res:
                res = prices[i] - local_min
        return res