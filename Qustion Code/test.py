from typing import List
from collections import defaultdict 

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        c = [0]*(len(nums)+1)
        ret = [0]*len(nums)

        def LowBit(x:int)->int:
            return x&(-x)
        
        def Update(n:int, pos:int):
            while (pos < n):
                c[pos] += 1
                pos += LowBit(pos)
        
        def Query(pos:int)->int:
            x = 0

            while pos > 0:
                x += c[pos]
                pos -= LowBit(pos)
            
            return x

        def lower_bound(n:int, x:int)->int:
            low = 0
            high = n - 1
            ans = 0
            while low <= high:
                mid = (low + high)//2
                if a[mid] <= x:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        def Discretization(n:int) -> int:
            m = 0
            for i in range(1,n):
                if a[i] > a[m]:
                    m += 1
                    a[m] = a[i]
            return m + 1
        
        m = Discretization(len(nums))
        for i in range(len(nums)-1,-1,-1):
            idx = lower_bound(m,nums[i])
            ret[i] = Query(idx-1+1)
            Update(m+1,idx+1)
        
        return ret
        

                    

if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5,2,6,1]))
