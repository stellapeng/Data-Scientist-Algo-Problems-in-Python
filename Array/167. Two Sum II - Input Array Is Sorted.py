# method 1:
# use two index, take advantage of the sorted list
# note: focus on this Two Pointers approach above. It's easier to get it right and adapt for other variations of 3Sum. 
# Time Complexity: O(n)
# Space Complexisty: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
		low = 0
		high = len(numbers) - 1

		while (low < high):
		    s = numbers[low] + numbers[high]
		    
		    if s == target:
		        return [low+1, high+1] 
		    
		    elif s < target:
		        low += 1
		        
		    else:
		        high -= 1
		    
		return [-1, -1]


# method 2:
# hashtable - the same as Two Sum
# Time Complexity: O(n)
# Space Complexisty: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
		# dictionary
        d = {}
        for i, v in enumerate(numbers):
             if target - v in d:
                return [d[target-v]+1, i+1]
             d[v] = i
        return [-1, -1]