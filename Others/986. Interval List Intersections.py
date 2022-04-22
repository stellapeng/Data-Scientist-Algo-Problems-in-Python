# Time complexity: O(m+n) m and n are the length of firstList and secondList
# Space complexity: O(m+n)

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1 = len(firstList)
        l2 = len(secondList)
        
        # use two pointers
        i, j = 0, 0
        res = []
        while (i < l1 and j < l2):
            a1, a2 = firstList[i][0],  firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            # it's easy to list the two cases that there are no intersections:
            # a2 < b1 or a1 > b2
            # take the negation of no intersections cases leads to the cases intersection exsited
            if (a2 >= b1 and a1 <= b2):
                res.append([max(a1, b1), min(a2, b2)])
            
            if a2 > b2:
                j+=1
            else:
                i+=1
        return res
                
            