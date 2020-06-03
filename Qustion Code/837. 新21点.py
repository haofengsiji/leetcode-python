# method_1
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0]*(K + W + 1)
        # init
        for i in range(K,min(N,K+W-1)+1):
                dp[i] = 1

        # DP
        for i in range(K-1,-1,-1):
            if i == K-1:
                for j in range(1,W+1):
                    dp[i] += 1/W*dp[i+j]
            # 差分优化
            else:
                dp[i] = dp[i+1] + 1/W*(dp[i+1] - dp[i+W+1])
        return dp[0]

# method_2
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (N + W + 1)
        
        for k in range(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        for k in range(K-1,-1,-1):
            dp[k] = S/W
            S += dp[k] - dp[k+W]

        return dp[0]