# Time Complexity: O(n), n = len(nums2)
# each element in nums2 is pushed once and poped once

# Space Complexity: O(n), dictionary stores n key-value pairs

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        s = []
        d = defaultdict()
        
        for i in range(len(nums2)-1, -1, -1):
            while (s and s[-1] <= nums2[i]):
                s.pop()
            d[nums2[i]] = s[-1] if s else -1
            s.append(nums2[i])

            
        for i in range(len(nums1)):
            res[i] = d[nums1[i]]
            
        return res

