# method_1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(dp[j]+1, max_len)
            dp[i] = max_len
        return max(dp)

# mehtod_1.1 6个月后
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

# method_2


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for num in nums:
            if not d or num > d[-1]:
                d.append(num)
            else:
                low = 0
                high = len(d) - 1
                loc = high
                while low <= high:
                    mid = (low + high)//2
                    if d[mid] >= num:
                        loc = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                d[loc] = num
        return len(d)
