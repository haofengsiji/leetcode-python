class Solution:
    def test(self, nums):
        nums.sort(key=lambda x: (x[1],x[0]))
        ans = [nums[0]]
        for i in range(1,len(nums)):
            if ans[-1][-1] < nums[i][0]:
                ans.append(nums[i])
        return ans


 

if __name__ == "__main__":
    s = Solution()
    print(s.test([[1,2],[3,4],[2,3]]))

