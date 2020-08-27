from typing import List
from collections import defaultdict 
import sys

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        if m == 0: return []
        n = len(image[0])
        visited = [[0]*n for _ in range(m)]
        org_val = image[sr][sc]

        def dfs(row,col):
            if 0 <= row < m and 0 <= col < n:
                if visited[row][col]: return
                visited[row][col] = 1
                d = [(0,1),(0,-1),(1,0),(-1,0)]
                if image[row][col] == org_val:
                    image[row][col] = newColor
                    for dx,dy in d:
                        dfs(row+dx,col+dy)
            return 
        
        dfs(sr,sc)

        return  image
                
                    

if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
