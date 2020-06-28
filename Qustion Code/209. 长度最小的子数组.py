# method_1 超时，C不超时
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

# method_2
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        start = 0
        end = 0
        n = len(nums)
        ans = n + 1
        prefix = nums[0]
        while True:
            if prefix < s:
                end += 1
                if end == n:
                    break
                prefix += nums[end]
            else:
                ans = min(ans,end-start+1)
                prefix -= nums[start]
                start += 1
                if start > end:
                    break
        if ans == n + 1:
            ans = 0
        return ans 

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        start = 0
        end = 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return ans if ans != n+1 else 0

# method_3
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n+1
        prefix = [0]*(n+1)
        # 求前缀和
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        for i in range(n):
            low = 0
            high = i
            while low <= high:
                mid = (low + high)//2
                if prefix[i+1] - s == prefix[mid]:
                    ans = min(ans,i-mid+1)
                    break
                elif prefix[i+1] - s > prefix[mid]:
                    ans = min(ans,i-mid+1)
                    low = mid + 1
                else:
                    high = mid - 1
        return ans if ans != n+1 else 0
