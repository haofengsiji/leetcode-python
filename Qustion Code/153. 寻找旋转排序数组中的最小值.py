# method_1:二分法
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        if right < 0: return []
        while left < right:
            mid = (left + right)//2 
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
# method_2:遍历
# 反而更快，但最坏O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0: return []
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
# method_3: min
# 笔试
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)