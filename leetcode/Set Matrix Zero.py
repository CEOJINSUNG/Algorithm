class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_position = []
        row = set()
        col = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                
                if i in row: 
                    matrix[i][j] = 0
                if j in col:
                    matrix[i][j] = 0