from typing import List
from collections import defaultdict 
import sys

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        ans = 1
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(j,-1,-1):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                        ans = max(dp[i][j],ans)
                    else:
                        dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return ans
                
                    

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("aaa"))
