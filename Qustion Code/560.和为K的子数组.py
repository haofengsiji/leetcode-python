# method_1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        len_nums = len(nums)
        for i in range(len_nums):
            for j in range(i+1):
                if sum(nums[j:i+1]) == k:
                    cnt += 1                  
                else:
                    continue
        return cnt

# method_2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        mp = {0:1}
        prefix = 0
        for num in nums:
            prefix += num
            # search
            if prefix - k in mp:
                cnt += mp[prefix - k]
            # update
            mp[prefix] = mp.setdefault(prefix, 0) + 1
        return cnt