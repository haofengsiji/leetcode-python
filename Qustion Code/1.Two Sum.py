"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if target - nums[i] in dict1:
                j = dict1.get(target - nums[i])
                return [j,i]
            dict1[nums[i]] = i
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        # Try one by one
        # time complexity: n^2
        # space complexity: 1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """

        # The implementation as below is bit tricky. but not difficult to understand
        #  1) loop though the array 
        #  2) just put the `target - num[i]`(not `num[i]`) into the map
        # @haoel's thoughts[https://github.com/haofengsiji/leetcode/blob/master/algorithms/cpp/twoSum/twoSum.cpp]
        # Code reference from @qiyuangong's code [https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py]
        hash_nums={}
        for index, num in enumerate(nums):
            another = target - num
            try:
                hash_nums[another]
                return [hash_nums[another],index]
            except KeyError:
                hash_nums[num] = index
