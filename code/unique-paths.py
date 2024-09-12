class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0): 
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-2] + matrix[m-2][n-1]
                    
