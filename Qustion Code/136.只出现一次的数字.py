# method 1
#   time O(n), space O(n)
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for key in hashmap:
            if hashmap[key] == 1:
                return key

# method 2
# time O(n), space O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] ^= nums[i]
        return nums[0]