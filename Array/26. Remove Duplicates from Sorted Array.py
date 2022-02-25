'''
Painpoints:
We need to modify the array in-place; 
However, the size of the final array would potentially be smaller than the size of the input array
'''

'''
Solution idea:
The solution is to use a two-pointer approach here. 
index j, would keep track of the current element in the original array, 
index i, is to track the unique elements.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        
        for j in range(len(nums)):
            if nums[i] != nums[j] and j>i:
                nums[i+1] = nums[j]
                i+=1
                
        return i+1
    