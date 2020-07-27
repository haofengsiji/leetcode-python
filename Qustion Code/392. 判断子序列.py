# method_1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        s_l = len(s)
        t_l = len(t)
        while i < s_l and j < t_l:
            if s[i] == t[j]:
                i += 1
            j += 1

        
        return i == s_l
        
# method_2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        f = [[0]*26 for _ in range(m)]
        f.append([m]*26)

        # 预处理t
        for i in range(m-1,-1,-1):
            for j in range(26):
                if ord(t[i]) - ord('a') == j:
                    f[i][j] = i
                else:
                    f[i][j] = f[i+1][j]
        
        add = 0
        for i in range(n):
            if f[add][ord(s[i])-ord('a')] == m:
                return False
            else:
                add = f[add][ord(s[i])-ord('a')] + 1

        return True
        