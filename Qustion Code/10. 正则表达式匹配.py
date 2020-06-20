# method_1
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        try:
            if s[re.match(p, s, flags=0).span()[0]:re.match(p, s, flags=0).span()[1]] == s:
                return True
            else:
                return False
        except:
            return False

# # method_2(too slow)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s # p = '' s =''
        first_match = bool(s) and p[0] in [s[0],'.']

        if len(p) >= 2 and p[1] == '*':
            return(self.isMatch(s,p[2:]) or 
                    first_match and self.isMatch(s[1:],p))
        else:
            return (first_match and self.isMatch(s[1:],p[1:]))

# # method_3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]

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
                    if Match(i,j-1):
                        dp[i][j] |= dp[i-1][j]
                elif Match(i,j):
                    dp[i][j] |= dp[i-1][j-1]
        
        return dp[n][m]
