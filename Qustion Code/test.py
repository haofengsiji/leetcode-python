class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cnt = 0
        len_nums = len(nums)
        nums.sort()
        for i in range(len_nums):
            for j in range(i,len_nums):
                if sum(nums[i:j+1]) == k:
                    cnt += 1
                elif sum(nums[i:j+1]) < k:
                    continue
                else:
                    break
        return cnt


 

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,2,1,2,1],3))

