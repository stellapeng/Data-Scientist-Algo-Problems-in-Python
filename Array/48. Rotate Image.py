# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def transpose(self, matrix:List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):  # upper triangle
            # or for j in range(i+1): # lower triangle
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    def reverse(self, matrix:List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reverse(matrix)
                