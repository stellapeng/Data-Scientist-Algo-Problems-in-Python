# method 1:
# use two index, take advantage of the sorted list
# note: focus on this Two Pointers approach above. 
# It's easier to get it right and adapt for other variations of 3Sum like 3Sum Smaller and 3Sum Closest

# Time Complexity: O(n^2)
# Space Complexisty: O(logn) to O(n), depending on the implementation of the sorting algorithm.
class Solution:
    def twoSum(self, nums, target):
        low, high = 0, len(nums)-1
        res = []
        while(low<high):
            left, right = nums[low], nums[high]
            s = nums[low] + nums[high]
            if(s<target):
                while(low<high and nums[low]==left):
                    low+=1
            if(s>target):
                while(low<high and nums[high]==right):
                    high-=1
            if(s==target):
                res.append([left, right])
                while(low<high and nums[low]==left):
                    low+=1
                while(low<high and nums[high]==right):
                    high-=1
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        i = 0
        while (i<n-2):
            sub_res = self.twoSum(nums[i+1:], -nums[i])
            if sub_res:
                print(sub_res)
                for j in sub_res:
                    r = [nums[i]] + j
                    res.append(r)
            
            while (i < n - 2 and nums[i] == nums[i + 1]):
                i+=1
                
            i += 1
        return res


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