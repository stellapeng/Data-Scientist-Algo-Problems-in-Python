# Trick: cache prefix sum
# Time Complexity: O(nm)
# Space Complexity: O(nm)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix is None or matrix[0] is None: 
            return None
        
        row = len(matrix)
        col = len(matrix[0])
        self.preSum = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.preSum[i][j] = self.preSum[i-1][j] + \
                                    self.preSum[i][j-1] + \
                                    matrix[i-1][j-1] - \
                                    self.preSum[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        ans = self.preSum[row2+1][col2+1] - \
              self.preSum[row1][col2+1] - \
              self.preSum[row2+1][col1] + \
              self.preSum[row1][col1]
        
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)




