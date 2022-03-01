# method 1.1:
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k in d:
            if d[k] == 1:
                return k


# method 1.2:
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # defaultdict never raise KEYERROR
        # change to other default value, use: defaultdict(lambda:1)
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        for k in d:
            if d[k] == 1:
                return k


# method 2:
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)



# method 3: 
# Time Complexity: O(n)
# Space Complexity: O(1)
# notes: 
# a XOR a = 0
# a XOR 0 = a
# XOR is associative

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i   # exlcusive or, XOR, res = res ^ i
        return res
