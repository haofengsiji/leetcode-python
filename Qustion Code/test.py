class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            # 头部去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n-1
            while L < R:
                # 中间部去重
                if L > i+1 and nums[L] == nums[L-1]:
                    L += 1
                # 无重复，且存在三元素和为零
                elif nums[i] + nums[L] + nums[R] == 0:
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                # 向左移
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    raise NameError
        return ans
if __name__ == "__main__":
    s = Solution()

    print(s.threeSum([-2,0,1,1,2]))