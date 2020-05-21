import collections
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)
        dp = [[None]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i==j+1 or i==j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i-1][j+1]
                else:
                    dp[i][j] = False
                # update ans
                if dp[i][j] == True and i-j+1 > len(ans):
                    ans = s[j:i+1]
        return ans 


 

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("cbbd"))

