from typing import List
from collections import defaultdict 
import sys

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[sys.maxsize]*(n+1) for _ in range(m)]

        sub = [0]
        for i in range(n):
            sub.append(sub[-1]+nums[i])

        dp[0][0] = 0
        for i in range(1,n):
            for j in range(1,min(i+1,m)):
                for k in range(1,i+1):
                    dp[j][i] = min(dp[j][i],max(dp[j-1][i-k],sub[i]-sub[i-k]))
        
        return dp[m][n]
        
if __name__ == "__main__":
    s = Solution()
    print(s.splitArray([7,2,5,10,8],2))
