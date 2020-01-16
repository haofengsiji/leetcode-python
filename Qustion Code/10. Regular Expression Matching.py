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
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not p: return not s # p = '' s =''
#         first_match = bool(s) and p[0] in [s[0],'.']

#         if len(p) >= 2 and p[1] == '*':
#             return(self.isMatch(s,p[2:]) or 
#                     first_match and self.isMatch(s[1:],p))
#         else:
#             return (first_match and self.isMatch(s[1:],p[1:]))

# # method_3
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         s_size = len(s)
#         p_size = len(p)

#         dp = [[False]*(p_size+1) for _ in range(s_size+1)]

#         for i in range(s_size,-1,-1):
#             for j in range(p_size,-1,-1):
#                 if not p[j:]: 
#                     dp[i][j] = not s[i:]
#                 else:
#                     first_match = bool(s[i:]) and p[j] in [s[i],'.']
#                     if len(p[j:]) >= 2 and p[j+1] == '*':
#                         dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
#                     else:
#                         dp[i][j] = first_match and dp[i+1][j+1]
            
#         return dp[0][0]
