## method 1:
# the built-in sort() funciton is in-place sorting
# time complexity: O((m+n)log(m+n))
# space complexity: O(n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()

        
## method 2:
# Three pointers, forward filling
# time complexity: O(m+n)
# space complexity: O(m) 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """    
        i, j = 0, 0
        nums1_copy = nums1[:m]
        
        for k in range(m+n):
            if (j == n) or ( i < m and nums1_copy[i] <= nums2[j]):
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
        

## method 3:
# Three pointers, backward filling
# time complexity: O(m+n)
# space complexity: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """    
        i, j = m - 1, n - 1
 
        for k in range(m + n - 1, -1, -1):
            if j < 0:     # nums1[0:(k+1)] is already sorted
                break
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            

