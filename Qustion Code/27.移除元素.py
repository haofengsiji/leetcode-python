# method_1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        j = n-1
        while i <= j:
            if nums[i] != val:
                i += 1
            else:
                if nums[j] == val:
                    j -=1
                else:
                    nums[i] = nums[j]
                    nums[j] = val
        return i