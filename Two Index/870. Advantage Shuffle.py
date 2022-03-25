# Time Complexity: O(nlogn)
# Space Complexity: O(n)
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_cp = []
        for i in range(len(nums2)):
            nums2_cp.append([i, nums2[i]])
        
        # nums2: descending order
        nums2_cp = sorted(nums2_cp,  key=lambda x: x[1], reverse=True)
        
        # nums1: ascending order
        nums1 = sorted(nums1)
        
        left, right = 0, len(nums1) - 1
        res = [0] * len(nums2)
        
        while(nums2_cp):
            pair = nums2_cp.pop(0)
            ind, maxval = pair[0], pair[1]
            
            if (nums1[right] > maxval):
                res[ind] = nums1[right]
                right -= 1
            else:
                res[ind] = nums1[left]
                left += 1
                
        return res
                