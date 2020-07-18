# method_1
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m+n != len(s3): return False

        f = [[False]*(n+1) for _ in range(m+1)]

        f[0][0] = True

        # First row
        for j in range(1,n+1):
            f[0][j] = f[0][j-1] & (s1[j-1] == s3[j-1])

        # First coloum
        for i in range(1,m+1):
            f[i][0] = f[i-1][0] & (s2[i-1] == s3[i-1])

        for i in range(1,m+1):
            for j in range(1,n+1):
                f[i][j] = (f[i][j-1] & (s1[j-1] == s3[i+j-1])) | (f[i-1][j] & (s2[i-1] == s3[i+j-1]))

        return f[-1][-1]

# method_2
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3): return False
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i > 0:
                    dp[j] &= s1[i-1] == s3[i+j-1]
                if j > 0:
                    dp[j] |= dp[j-1] and s2[j-1] == s3[i+j-1]
        
        return dp[-1]
                