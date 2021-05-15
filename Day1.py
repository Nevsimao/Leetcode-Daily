# Group Anagrams

## Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

### Solution (Python)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag, rows, cols = 1, len(matrix), len(matrix[0])
        for i in range(0, rows):
            if matrix[i][0] == 0:
                flag = 0
            for x in range(1, cols):
                if matrix[i][x] == 0:
                    matrix[i][0] = matrix[0][x] = 0
        for i in range(rows - 1, -1, -1):
            for x in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][x] == 0:
                    matrix[i][x] = 0
            if flag == 0:
                matrix[i][0] = 0
        return matrix
