# method_1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

# method_2
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

# method_3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1]*m
        for i in range(1,n):
            for j in range(1,m):
                cur[j]  = cur[j-1] + cur[j]
        return cur[-1]