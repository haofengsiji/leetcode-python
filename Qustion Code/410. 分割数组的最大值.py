# method_1
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[sys.maxsize]*(m+1) for _ in range(n+1)]

        sub = [0]
        for num in nums:
            sub.append(sub[-1]+num)

        dp[0][0] = 0
        for i in range(1,n+1):
            for j in range(1,min(i,m)+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1],sub[i]-sub[k]))
        
        return dp[n][m]

# method_2
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 确定二分范围[max(nums),sum(nums)]
        left = max(nums)
        right = sum(nums)

        def check(x):
            subSum = 0
            cnt = 1
            for num in nums:
                subSum += num
                if subSum > x:
                    subSum = num
                    cnt += 1
            
            return cnt <= m

        ans = left        
        while left <= right:
            mid = (left + right)//2
            if check(mid):
                # 如果按照mid 分组 <= m, 则说明 mid值取大了
                ans = mid
                right = mid - 1
            else:
                # 如果按照mid 分组 > m, 则说明 mid值取小了
                left = mid + 1
            
        return ans