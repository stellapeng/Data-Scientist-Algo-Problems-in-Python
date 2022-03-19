# cache array diff
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0]*length
        
        for l in updates:
            i = l[0]
            j = l[1]
            val = l[2]
            
            diff[i] += val
            if j+1 <= length-1:
                diff[j+1] -= val
        
        res = []
        for i, v in enumerate(diff):
            if i == 0:
                res.append(v)
            else:
                res.append(res[i-1] + v)
                
        return res

# Alternative increment loopL
        # res = [0]*length
        # res[0] = diff[0]
        # for i in range(1, length):
        #     res[i] = res[i-1] + diff[i]

        
        