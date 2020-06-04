# method_1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1]*n
        R = [1]*n
        ans = [0]*n
        # 计算前缀后缀乘积
        for i in range(1,n):
            L[i] = L[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            R[i] = R[i+1]*nums[i+1]
        
        for i in range(n):
            ans[i] = L[i]*R[i]

        return ans

# method_2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        left = 1
        right = 1
    
        for i in range(n):
            ans[i] *= right
            ans[-1-i] *= left
            right *= nums[i]
            left *= nums[-1-i]

        return ans