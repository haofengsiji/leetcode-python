# method_1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        dp = [1,2]
        dp = [1,2] + [None for _ in range(n-2)]
        for i in range(2,n):
            # 走一步到达i，走两步到达i
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

# method_2
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        ans = [1,2]
        for i in range(2,n):
            temp = ans[0] + ans[1]
            ans = ans[1:] + [temp]
        return ans[-1]

# method_3
class Solution:
    def climbStairs(self, n: int) -> int:
        # 归
        if n == 0:
            return 1
        if n < 0:
            return 0
        # 递
        return self.climbStairs(n-1) + self.climbStairs(n-2)