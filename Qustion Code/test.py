class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[-1][-1] = max(1,-dungeon[-1][-1])
        for i in range(rows-2,-1,-1):
            dp[i][-1] = max(1,min(dp[i+1][-1],dp[i+1][-1]-dungeon[i][-1]))
        for j in range(cols-2,-1,-1):
            dp[-1][j] = max(1,min(dp[-1][j+1],dp[-1][j+1]-dungeon[-1][j]))
            
        for i in range(rows-2,-1,-1):
            for j in range(cols-2,-1,-1):
                dp[i][j] = max(1,min(min(dp[i+1][j],dp[i][j+1]),min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]))
               
        return dp

if __name__ == "__main__":
    s = Solution()
    print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))

