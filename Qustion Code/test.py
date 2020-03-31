import random
class Solution:
    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums)-1)
        return nums

    
    def randomized_quicksort(self,nums,start,end):
        if start >= end:
            return
        pivot = self.randomized_partition(nums,start,end)
        self.randomized_quicksort(nums,start,pivot-1)
        self.randomized_quicksort(nums,pivot+1,end)
    
    def randomized_partition(self,nums,start,end): 
        pivot = random.randint(start,end) # random range [start,end]
        nums[pivot],nums[end] = nums[pivot],nums[end]
        i = start -1
        for j in range(start,end):
            if  nums[j] <= nums[end]:
                i += 1
                # swap
                nums[j], nums[i] = nums[i], nums[j]
        i = i+1
        # swap
        nums[j], nums[i] = nums[i], nums[j]
        return i


 

if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5,2,3,1]))

