# method_1
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        memo = [[None]*(n+2) for _ in range(n+2)]

        def solve(left:int, right:int) -> int:
            if left >= right - 1: return 0

            if memo[left][right]: return memo[left][right]

            best = 0
            for i in range(left+1,right):
                total = val[left]*val[i]*val[right]
                total += solve(left,i) + solve(i,right)
                best = max(total,best)
            
            memo[left][right] = best

            return best
        
        return solve(0,n+1)
        
# method_1.1
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            
            return best

        return solve(0, n + 1)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# method_2
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        for i in range(n-1,-1,-1):
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    total = val[i]*val[k]*val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(total,dp[i][j])
        
        return dp[0][n+1]