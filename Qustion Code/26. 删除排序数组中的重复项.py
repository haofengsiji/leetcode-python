# method_1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        while  j < n-1:
            if nums[j] == nums[j+1]:
                nums.pop(j)
                n = len(nums)
            else:
                j +=1
        return n

# method_2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        if n == 0: return 0
        
        for j in range(1,n):
            if nums[j] != nums[i]:
                i +=1
                nums[i] = nums[j]
            else:
                j +=1

        return i+1