from typing import List
from collections import defaultdict 

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums) 
        ans = n + 1
        for i in range(n):
            Sum = 0
            for j in range(i,n):
                Sum += nums[j]
                if Sum >= s:
                    ans = min(ans,j-i+1)
                    break
        if ans == n+1:
            ans = 0
        return ans
        

                    

if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(11,[1,2,3,4,5]))
