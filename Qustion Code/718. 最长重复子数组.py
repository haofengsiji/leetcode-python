# method_1: force
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        ans = 0
        for i in range(n):
            for j in range(m):
                k = 0
                while i+k<n and j+k <m and A[i+k] == B[j+k]:
                        k += 1
                ans = max(k,ans)
        return ans

# method_2: dp
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        ans = 0
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                    dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
                    ans = max(dp[i][j],ans)

        return ans

# method_3: sliding window
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def maxlength(addA,addB,length):
            max_k = 0
            k = 0
            for i in range(length):
                if A[addA+i] == B[addB+i]:
                    k += 1
                    max_k = max(max_k,k)
                else:
                    k = 0
            return max_k

        n = len(A)
        m = len(B)
        ans = 0
        for i in range(n):
            length = min(n-i,m)
            ans = max(ans,maxlength(i,0,length))
        for i in range(m):
            length = min(m-i,n)
            ans = max(ans,maxlength(0,i,length))
        return ans

# method_4: binary search + hash map
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def check(mid:int)->bool:
            base = 100
            mod = 10**9+9
            hashA = 0
            bucketA = set()
            for i in range(mid):
                hashA = (hashA*base + A[i]) % mod
            bucketA.add(hashA)
            mult = pow(base,mid-1,mod)
            for i in range(mid,len(A)):
                hashA = ((hashA - mult*A[i-mid])*base + A[i]) % mod
                bucketA.add(hashA)

            hashB = 0
            for i in range(mid):
                hashB = (hashB*base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(mid,len(B)):
                hashB = ((hashB - mult*B[i-mid])*base + B[i]) % mod
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