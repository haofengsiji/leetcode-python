# Method_1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = len(nums)
        dp_min = [nums[0]]*nums_len
        dp_max = [nums[0]]*nums_len
        for i in range(1,nums_len):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])    
        return max(dp_max)