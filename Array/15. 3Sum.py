# method 1:
# use two index, take advantage of the sorted list
# note: focus on this Two Pointers approach above. 
# It's easier to get it right and adapt for other variations of 3Sum like 3Sum Smaller and 3Sum Closest

# Time Complexity: O(n^2)
# Space Complexisty: O(logn) to O(n), depending on the implementation of the sorting algorithm.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            # Increment lo while the next value is the same to avoid duplicates in the result.
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res
    
    def twoSumII(self, nums: List[int], i: int, res:List[List[int]]) -> List[List[int]]:
        low, high = i+1, len(nums) - 1

        while (low < high):
            s = nums[i] + nums[low] + nums[high]
            if s < 0:
                low += 1
            elif s > 0:
                high -= 1
            else:
                print(s)
                res.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
                
                # Increment lo while the next value is the same to avoid duplicates in the result.
                while low < high and nums[low] == nums[low - 1]:
                    low += 1


# method 2:
# hashtable - the same as Two Sum

# Time Complexity: O(n^2), twoSum is O(n), and we call it n times.
# Space Complexisty: O(n) for the hashset
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break;
            # Increment lo while the next value is the same to avoid duplicates in the result.
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
    
    def twoSum(self, nums: List[int], i: int, res:List[List[int]]) -> List[List[int]]:
        # set is implemented as a hash table.
        seen = set() 
        j = i + 1
        while j < len(nums):
            complement = -(nums[i]+nums[j])
            if complement in d:
                res.append([nums[i], nums[j], complement])
                # Increment lo while the next value is the same to avoid duplicates in the result.
                 while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
            seen.add(nums[j])