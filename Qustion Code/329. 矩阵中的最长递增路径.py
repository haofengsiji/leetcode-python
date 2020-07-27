# method_1
class Solution:

    DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def dfs(row,col):
            res = 0
            for dx,dy in self.DIRS:
                new_row = row + dx
                new_col = col + dy
                if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m and matrix[new_row][new_col] > matrix[row][col] :
                    res = dfs(new_row,new_row) + 1
            
            return res
                 
        best = 0
        for i in range(n):
            for j in range(m):
               best =  max(best,dfs(i,j))
        
        return best

# method_2
