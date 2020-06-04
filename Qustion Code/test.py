class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        L = [nums[0]]*n
        R = [nums[-1]]*n
        ans = [0]*n
        # 计算前缀后缀乘积
        for i in range(1,n):
            L[i] = L[i-1]*nums[i]

        for i in range(n-2,-1,-1):
            R[i] = R[i+1]*nums[i]
        
        for i in range(1,n-1):
            ans[i] = L[i-1]*R[i+1]
        ans[0] = R[1]
        ans[-1] = L[-2]
        return ans,L,R


 

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))

