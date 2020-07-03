from typing import List
from collections import defaultdict 

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(mid:int)->bool:
            base = 100
            mod = 10**9+9
            hashA = 0
            bucketA = set()
            for i in range(mid):
                hashA = hashA*base + A[i]
            bucketA.add(hashA)
            for i in range(mid,len(A)):
                hashA = (hashA - base**(mid-1)*A[i-mid])*base + A[i]
                bucketA.add(hashA)

            hashB = 0
            for i in range(mid):
                hashB = hashB*base + B[i]
            if hashB in bucketA:
                return True
            for i in range(mid,len(B)):
                hashB = (hashB - base**(mid-1)*B[i-mid])*base + B[i]
                if hashB in bucketA:
                    return True
            
            return False
            
        
        n = len(A)
        m = len(B)
        low = 0
        high = min(n,m)
        ans = 0
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        

                    

if __name__ == "__main__":
    s = Solution()
    print(s.findLength([1,2,3,2,1],[3,2,1,4,7]))
