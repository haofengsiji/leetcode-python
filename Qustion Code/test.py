import collections
class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        # 分
        mid = len(nums)//2
        sorted_left = self.sortArray(nums[:mid])
        sorted_right = self.sortArray(nums[mid:])
        # 合
        return self.merge(sorted_left,sorted_right)

    def merge(self,left,right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left[0])
                left.pop(0)
            else:
                res.append(right[0])
                right.pop(0)
        if not left:
            res = res + right
        if not right:
            res = res + left
        return res


 

if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5,2,3,1]))

