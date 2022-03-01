# Time Complexity: O(n+m)
# Space Complexity: O(min(n, m))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # make sure the first list is no longer than the second list
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        d1 = Counter(nums1)
        res = []
        for i in nums2:
            if i in d1 and d1[i] > 0:
                res.append(i)
                d1[i] -= 1
        return res



# Time Complexity: O(nlog(n) + mlog(m))
# Space Complexity: O(n+m) -- python list built-in inplace sort method

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        res = []
        
        while (i < len(nums1) and j < len(nums2)):
            a = nums1[i]
            b = nums2[j]
            if a < b:
                i += 1
            elif a > b:
                j += 1
            else:
                res.append(a)
                i += 1
                j += 1
        return res


