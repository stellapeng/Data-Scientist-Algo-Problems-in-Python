# method 1:
# Time Complexity: O(nm)
# Space Complexity: O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_ind = set()
        c_ind = set()
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    r_ind.add(i)
                    c_ind.add(j)
        
        for i in r_ind:
            for j in range(ncol):
                matrix[i][j] = 0
        
        for j in c_ind:
            for i in range(nrow):
                matrix[i][j] = 0
 


# method 2:
# we can use the first cell of every row and column as a flag: 
# matrix[0][0] can be flag for either the first row or the first col
# we let matrix[0][0] to be the flag for the first row, 
# and use an additioanl boolean to be the flag for the first column
# Time Complexity: O(nm)
# Space Complexity: O(1)        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        is_col = False
        for i in range(nrow):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, ncol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, nrow):
            for j in range(1, ncol):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(ncol):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(nrow):
                matrix[i][0] = 0

