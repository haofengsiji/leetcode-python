class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Try one by one
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[i] + nums[j] == target:
                    return [i,j]