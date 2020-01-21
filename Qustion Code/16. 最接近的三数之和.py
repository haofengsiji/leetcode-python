# method_1
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序
        nums.sort()
        
        n = len(nums)
        ans = sum(nums[:3])

        # 特殊情况
        if n == 3:
            return ans

        # 双指针
        for i in range(n):
            L = i+1
            R = n - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s < target:
                    L +=1
                elif s > target:
                    R -=1
                else:
                    return s

        return ans