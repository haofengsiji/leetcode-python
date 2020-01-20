# method_1
#   归并排序，分治算法
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        # 分
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # 治
        return self.merge(left,right)

    def merge(self,left,right):
        result = []
        i,j =0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j +=1
        if i >= len(left): 
            return result + right[j:]
        else:
            return result + left[i:]