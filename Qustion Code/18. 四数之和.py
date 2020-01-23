class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            for j in range(i+1,n):
                if j - i > 1 and nums[j-1] == nums[j]:
                    continue
                L = j+1
                R = n-1
                while L < R:
                    s = nums[i] + nums[j] + nums[L] + nums[R]
                    if s == target:
                        ans.append([nums[i],nums[j],nums[L],nums[R]])
                        L +=1
                        R -=1
                        while L < R and nums[L] == nums[L-1]: L +=1
                        while L < R and nums[R] == nums[R+1]: R -=1
                    elif s > target:
                        R -=1
                    else:
                        L +=1
        return ans  