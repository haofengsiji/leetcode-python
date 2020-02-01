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