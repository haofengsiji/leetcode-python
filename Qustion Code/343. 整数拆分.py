# method_1
class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        for i in range(2,n+1):
            tmp = 1
            norm = n // i
            rem = n % i
            for j in range(i):
                if j < rem:
                    tmp = tmp * (norm + 1)
                else:
                    tmp = tmp * norm
            if tmp > ans:
                ans = tmp
            else:
                break
        return ans

# method_2
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

# method_3
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        
        return dp[n]

# method_4
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2