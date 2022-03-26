'''
Painpoints:
We need to modify the array in-place; 
However, the size of the final array would potentially be smaller than the size of the input array
'''

'''
Solution idea:
The solution is to use a two-pointer approach here. 
index fast, would keep track of the current element in the original array, 
index slow, is to track the unique elements.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                nums[slow+1] = nums[fast]
                slow+=1
                
        return slow+1

        