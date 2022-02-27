
# method 1.1
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:        
        k = k % len(nums)
        n = len(nums)
        nums_copy = nums.copy()

        for i in range(n):
            nums[(i + k) % n] = nums_copy[i]

# method 1.2

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:        
        k = k % len(nums)
        n = len(nums)
        nums_copy = nums.copy()
    
        for i in range(k):
            nums[i] = nums_copy[-(k-i)]
        
        for i in range(k, n):
            nums[i] = nums_copy[(i-k)]



# method 2.1
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
                
        n = len(nums)
        k = k % n
        
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


# method 2.2

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        n = len(nums)
        k = k % n
        
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


# method 3: Cyclic Replacements
## proof: https://massivealgorithms.blogspot.com/2014/06/rotate-array-right-by-k-element-without.html