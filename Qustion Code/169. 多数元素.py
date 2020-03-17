# method_1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        ans = None
        nums_cnt = collections.Counter(nums)
        for key in nums_cnt:
            if nums_cnt[key] >  n:
                ans = key
                break
        return ans
        
# method_1.1
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# method_2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]