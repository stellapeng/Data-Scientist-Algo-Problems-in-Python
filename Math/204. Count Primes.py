# Time complexity: O(nlog(n))
# Space complexity: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = [False, False] + [True] * (n-2)
        for p in range(2, int(sqrt(n))+1):
            if nums[p]:
                for i in range(p * p, n, p):  # wont go up to n, stricly less than n
                    nums[i] = False
        
        return sum(nums)


# dont use, too slow, O(n^2)
class Solution:
    def isPrime(self, num: int) -> bool:
        if num == 2:
            return True
        
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def countPrimes(self, n: int) -> int:
        cnt = 0
        if n <= 2:
            return cnt
        
        for num in range(2, n):
            if self.isPrime(num):
                cnt += 1
        return cnt