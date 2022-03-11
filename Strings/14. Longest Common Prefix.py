# method 1.1:
# Time Complexity: O(mn)
# Space Complexisty: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        
        minstr = len(strs[0])
        for i in range(n):
            if len(strs[i]) < minstr:
                minstr = len(strs[i])
        
        ans = ""
        for i in range(minstr):
            for j in range(n - 1):
                if strs[j][i] != strs[j+1][i]:
                    return ans
            else: ans += strs[0][i]
        return ans



# method 1.2: variant of 1.1, shorter syntax than 1.1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        minstr = len(min(strs, key=len))
        
        ans = ""
         
        for i in range(minstr):
            pf = strs[0][:(i+1)]
            for j in range(n):
                if not strs[j].startswith(pf):
                    
                    return ans
            else: ans += strs[0][i]
        return ans

# -------------------------------------------------------------------------




# method 2.1: enumerate(zip(*strs))        
# Time Complexity: O(mn)
# Space Complexisty: O(1)
# enumerate(zip(*strs)) returns index and tuple of characters from each word.
# strs = ["flower","flow","flight"]
# enumerate(zip(*strs)) = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')] 
def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    for i, letter_group in enumerate(zip(*strs)):
        # ["flower","flow","flight"]
        # print(i,letter_group,set(letter_group))
        # 0 ('f', 'f', 'f') {'f'}
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


# method: 2.2: variant of 2.1   
# Time Complexity: O(mn)
# Space Complexisty: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        letter_groups, longest_pre = zip(*strs), ""
        # print(letter_groups, longest_pre)
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')] 
        for letter_group in letter_groups:
            if len(set(letter_group)) > 1: break
            longest_pre += letter_group[0]
        return longest_pre

# -------------------------------------------------------------------------



# method 3.1:  
# only need to compare the min and max strings lexicographically 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = ""
        if not strs:
            return longest_pre
        
        min_s = min(strs)
        max_s = max(strs)
        
        for i in range(len(min_s)):
            if len(max_s) > i and max_s[i] == min_s[i]:
                longest_pre += max_s[i]
            else:
                return longest_pre
        return longest_pre


# method 3.2: use sort(), lexicographically
# only need to compare the first and last strings after sorting the list       
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_pre = ""
        if strs and len(strs) > 0:
            strs = sorted(strs) 
            # e.g. before sort: ["flower","flow","flight","fake"]
            # after sort: ['fake', 'flight', 'flow', 'flower']
            first, last = strs[0], strs[-1]
            for i in range(len(first)):
                if len(last) > i and last[i] == first[i]:
                    longest_pre += last[i]
                else:
                    return longest_pre
        return longest_pre

# -------------------------------------------------------------------------




# method 4.1: divide and conquer
# Time Complexity: O(mn)
# Space Complexisty: O(m*logn)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(left,right):
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]
        
        def find_longestCommonPrefix(strs, left, right):
            if left == right:
                return strs[left]
            # recursive call
            else:
                mid = (left + right)//2
                lcpLeft = find_longestCommonPrefix(strs,left, mid)
                lcpRight = find_longestCommonPrefix(strs,mid+1,right)
                return commonPrefix(lcpLeft,lcpRight)
        
        if not strs: 
            return ""
        else:
            return find_longestCommonPrefix(strs, 0, len(strs)-1)



# method 4.2: divide and conquer
# Time Complexity: O(mn)
# Space Complexisty: O(m*logn)
class Solution:
    def commonPrefix(self, left,right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    def find_longestCommonPrefix(self, strs, left, right):
        # base case
        if left == right:
            return strs[left]
        
        # recursive call
        else:
            mid = (left + right)//2
            lcpLeft = self.find_longestCommonPrefix(strs,left, mid)
            lcpRight = self.find_longestCommonPrefix(strs,mid+1,right)
            return self.commonPrefix(lcpLeft,lcpRight)
            
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if not strs: 
            return ""
        else:
            return self.find_longestCommonPrefix(strs, 0, len(strs)-1)

# -------------------------------------------------------------------------




# method 5: binary search
# Time Complexity: O(mn*log(m))
# Space Complexisty: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(strs: List[str], length: str) -> bool:
            strl = strs[0][:length]
            print(strl)
            for i in range(1,len(strs)):
                if not strs[i].startswith(strl):
                    return False
            return True

        if not strs: return ""
        minLen = len(min(strs, key=len))
        low, high = 1, minLen

        # the binary search on the length of prefix on the first word
        while(low <= high):
            mid = (low+high) // 2
            if (isCommonPrefix(strs, mid)):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:high]


