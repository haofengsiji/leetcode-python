# method_1
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans,self.dfs(grid,i,j))
        return ans
    def dfs(self,grid,cur_i,cur_j):
        # 当前为海，或者超出搜索域
        if cur_i < 0 or cur_j < 0 \
        or cur_i == len(grid) or cur_j == len(grid[0]) \
        or grid[cur_i][cur_j] == 0:
            return 0
        # 当前为岛屿，向四周搜索
        ans = 1
        grid[cur_i][cur_j] = 0 # 搜索过后标0，避免重新搜索
        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            # 搜索坐标
            next_i,next_j = cur_i+di,cur_j+dj
            ans += self.dfs(grid,next_i,next_j)
        return ans

# method_2
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = 0
                stack = [(i,j)]
                # dfs
                while stack:
                    cur_i,cur_j = stack.pop()
                    if cur_i >= 0 and cur_j >= 0 and cur_i < len(grid) and cur_j < len(grid[0]) and grid[cur_i][cur_j] == 1:
                        cur += 1
                        grid[cur_i][cur_j] = 0
                        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                            stack.append((cur_i+di,cur_j+dj))
                ans = max(ans,cur)
        return ans
# method_3
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = 0 
                q = collections.deque([(i,j)])
                while q:
                    cur_i,cur_j = q.popleft() # 广度优先，如果是pop就是深度优先
                    if cur_i >= 0 and cur_j >= 0 and cur_i < len(grid) and cur_j < len(grid[0]) and grid[cur_i][cur_j] == 1:
                        cur += 1
                        grid[cur_i][cur_j] = 0
                        for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                            q.append((cur_i+di,cur_j+dj))
                ans = max(cur,ans)
        return ans