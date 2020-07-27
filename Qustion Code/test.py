from typing import List
from collections import defaultdict 
import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = []

        def dfs(row,col,res,visited):
            nonlocal ans,n,m,matrix
            # 防止越界
            if row >= n or row < 0 or col >= m or col <0 or visited[row][col]:
                # 越界，更新答案
                if len(res)-1 > len(ans):
                    ans = res[1:]
            else:
                # 没有越界，处理当前值
                num  = matrix[row][col]
                visited[row][col] = 1
                if num > res[-1]:
                    # 符合条件
                    res.append(num)
                    # 向四周搜索
                    dfs(row+1,col,res,visited)
                    dfs(row-1,col,res,visited)
                    dfs(row,col+1,res,visited)
                    dfs(row,col-1,res,visited)
                else:
                    # 不符合条件，更新答案
                    if len(res)-1 > len(ans):
                        ans = res[1:]

            return
            
        for i in range(n):
            for j in range(m):
                visited = [[0]*m for _ in range(n)]
                dfs(i,j,[-1],visited)
        
        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
