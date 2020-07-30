from typing import List
from collections import defaultdict 
import sys

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

if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(8))
