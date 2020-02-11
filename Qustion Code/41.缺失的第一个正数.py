class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 保证有1
        if 1 not in nums:
            return 1
        
        n = len(nums)
        
        # 保证都在1~n的范围内
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # 以自身正负为bitmap，标记
        for i in range(n):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        
        # 找到第一个为正的索引，即使没有出现的最小正数
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        # 全为负
        return n+1