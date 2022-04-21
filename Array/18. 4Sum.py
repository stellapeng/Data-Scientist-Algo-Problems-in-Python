# generic solution for nSum problems

# Time Complexity: O(m^(n-1)), n = 4 for 4Sum

class Solution:
    
    def nSumTarget(self, nums, n, start, target):
        sz = len(nums)
        res = []
        
        if (n<2 or sz<n):
            return res
        
        if (n==2):
            low, high = start, sz-1
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
        else:
            i = start
            while (i<sz):
                sub_res = self.nSumTarget(nums, n-1, i+1, target-nums[i])
                if sub_res:
                    for j in sub_res:
                        r = [nums[i]] + j
                        res.append(r)
                while (i < sz - 1 and nums[i] == nums[i + 1]):
                    i+=1
                i += 1
        
        return res
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return self.nSumTarget(nums, 4, 0, target)
        