class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <=1: return nums
        flag = False
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                flag = True
                break
        dec_i = i-1
        for i in range(dec_i+1,n):
            if nums[i] > nums[dec_i]:
                if len(nums[i:]) == 1 or nums[dec_i] >= nums[i+1]:
                    tmp = nums[dec_i]
                    nums[dec_i] = nums[i]
                    nums[i] = tmp
                    break
        if flag == False: dec_i = -1
        # reverse 就行了
        i = dec_i+1
        j = n-1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i +=1
            j -=1
        # 冒泡排序
        # for i in range(n-1,dec_i,-1):
        #     for j in range(dec_i+1,i):
        #         if nums[j] > nums[j+1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = tmp
