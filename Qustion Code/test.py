class Solution:
    def nextPermutation(self, nums) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            n = len(nums)
            for i in range(n-1,0,-1):
                if nums[i] > nums[i-1]:
                    break
            dec_i = i-1
            for i in range(dec_i+1,n):
                if nums[dec_i] >= nums[i] and nums[dec_i] < nums[i+1]:
                    tmp = nums[dec_i]
                    nums[dec_i] = nums[i]
                    nums[i] = tmp
                    break
            for i in range(n-1,dec_i,-1):
                for j in range(dec_i+1,i):
                    if nums[j] > nums[j+1]:
                        tmp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = tmp


        
                    

if __name__ == "__main__":
    s = Solution()

    print(s.nextPermutation([1,2,3]))