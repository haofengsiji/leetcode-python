from typing import List
from collections import defaultdict 
# Definition for a binary tree node.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]

        def Match(i,j):
            if i == 0:
                return False
            elif p[j-1] in [s[i-1],'.']:
                return True
            else:
                return False
                
        dp[0][0] = True
        for i in range(n+1):
            for j in range(1,m+1):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    if Match(i,j):
                        dp[i][j] |= dp[i-1][j]
                elif Match(i,j):
                    dp[i][j] |= dp[i-1][j-1]
        
        return dp[n][m]
            
        

                    

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aaa","ab*a*c*a"))
