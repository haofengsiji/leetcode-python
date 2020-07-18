from typing import List
from collections import defaultdict 

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if m+n != len(s3): return False

        f = [[False]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    f[i][j] = True
                elif i == 0:
                    f[i][j] = f[i][j-1] & (s1[j-1] == s2[i+j-1])
                elif j == 0:
                    f[i][j] = f[i-1][j] & (s2[i-1] == s2[i+j-1])
                else:
                    f[i][j] = (f[i][j-1] & (s1[j-1] == s2[i+j-1])) | (f[i-1][j] & (s2[i-1] == s2[i+j-1]))

        return f[-1][-1]
        
if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc","dbbca","aadbbcbcac"))
