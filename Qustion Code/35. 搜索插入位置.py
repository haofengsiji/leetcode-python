# method_1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1 
        low = 0
        ### 优化
        if target < nums[0]:
            return 0
        if target > nums[high]:
            return high+1
        ###
        while low <= high:
            mid = (high+low)//2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        return low # low 为刚好大于target的位置索引
        # return high 则返回刚好小于target的位置索引

# method_2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i +=1
            else:
                break
        return i