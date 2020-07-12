# method_1
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        # 从左下角到右上角，后方的加血对前方的扣血是没有用的
        # 从右上角到左下角，后方的加血对前方的扣血是有用的
        # 所以我们采取从左下角到右上角
        dp = [[None for _ in range(cols)] for _ in range(rows)]
    
        dp[-1][-1] = max(1,1-dungeon[-1][-1])
        for i in range(rows-2,-1,-1):
            dp[i][-1] = max(1,dp[i+1][-1]-dungeon[i][-1])
        for j in range(cols-2,-1,-1):
            dp[-1][j] = max(1,dp[-1][j+1]-dungeon[-1][j])
        
        for i in range(rows-2,-1,-1):
            for j in range(cols-2,-1,-1):
                dp[i][j] = max(1,min(dp[i+1][j]-dungeon[i][j],dp[i][j+1]-dungeon[i][j]))
        
        return dp[0][0]

# method_1.1
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        BIG = 10**9
        dp = [[BIG]*(n+1) for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                minn = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(minn-dungeon[i][j],1)
        
        return dp[0][0]

# method_2 未优化
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        def dfs(i,j):
            # 到达最后一行，最后一列
            if i == m-1 and j == n-1:
                return max(1 - dungeon[i][j],1)
            # 到达最后一行,向右搜索
            if i == m-1:
                return max(dfs(i,j+1) - dungeon[i][j],1)
            # 到达最后一列，向下搜索
            if j == n-1:
                return max(dfs(i+1,j) - dungeon[i][j],1)
            
            # 向右+向下搜索
            return max(min(dfs(i,j+1) - dungeon[i][j],dfs(i+1,j) - dungeon[i][j]), 1)
        
        return dfs(0,0)

# method_2.1 memo 优化
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        memo = [[0]*n for _ in range(m)]
        
        def dfs(i,j):
            # 到达最后一行，最后一列,终点
            if i == m-1 and j == n-1:
                return max(1 - dungeon[i][j],1)
            
            # 查询当前结果
            if memo[i][j] > 0:
                return memo[i][j]

            # 到达最后一行,向右搜索
            if i == m-1:
                minRes = max(dfs(i,j+1) - dungeon[i][j],1)
            # 到达最后一列，向下搜索
            elif j == n-1:
                minRes = max(dfs(i+1,j) - dungeon[i][j],1)
            else:
            # 向右+向下搜索
                minRes = max(min(dfs(i,j+1) - dungeon[i][j],dfs(i+1,j) - dungeon[i][j]), 1)
            
            # 记录当前结果
            memo[i][j] = minRes

            return minRes

        return dfs(0,0)