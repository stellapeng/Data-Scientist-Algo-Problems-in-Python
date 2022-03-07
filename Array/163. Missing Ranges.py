# the key of this point is to add lower - 1 and upper + 1 to the list
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        res = []
        
        for i in range(len(nums)-1):
            
            if nums[i+1] - nums[i] > 1:
                start = str(nums[i] + 1)
                end = str(nums[i+1] - 1)
                
                if start == end:
                    res.append(start)
                else:
                    res.append(start+"->"+end)
        return res

        