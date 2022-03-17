# method 1:
# use sort tuple or string as the dictionary key
# Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs.
# The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
# Space Complexity: O(NK), the total information content stored in ans. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
      
        for s in strs:
            # return tuple as ('a','e','t'), list and set are unhashble
            # ans[tuple(sorted(s))].append(s) 
            ans[''.join(sorted(s))].append(s) # return strings as 'aet'
            
        return ans.values()
    

# method 2:
# use counter tuple as the key
# Time Complexity: O(NK)
# Space Complexity: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
         


# method 3:
# use counter tuple as the key, and python Counter function to produce the counter
# Time Complexity: O(N(K+KlogK), (KlogK) is the Counter sort time
# Space Complexity: O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        ans = defaultdict(list)
        
        for s in strs:
            c = Counter(s)
            k = tuple(sorted(c.items(), key=itemgetter(0)))
            ans[k].append(s)
        return ans.values()   

