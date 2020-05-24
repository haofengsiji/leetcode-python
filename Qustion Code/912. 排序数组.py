# method_1
#   归并排序，分治算法
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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

# # method_2
# #   冒泡：超时
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         i = 0
#         j = n-1
#         for j in range(n-1,-1,-1):
#             for i in range(j):
#                 if nums[i] > nums[i+1]:
#                     t = nums[i]
#                     nums[i] = nums[i+1]
#                     nums[i+1] = t
#         return nums

# # method_3
# #   快排
# class Solution:
#     def sortArray(self, nums):
#         self.nums = nums
#         self.quicksort(0,len(nums)-1)
#         return self.nums

    
#     def quicksort(self,start,end):
#         if start < end:
#             pivot = self.partition(start,end)
#             self.quicksort(start,pivot-1)
#             self.quicksort(pivot+1,end)


    
#     def partition(self,start,end): 
#         i = start -1
#         for j in range(start,end):
#             if self.nums[j] <= self.nums[end]:
#                 i += 1
#                 # swap
#                 tmp = self.nums[j]
#                 self.nums[j] = self.nums[i]
#                 self.nums[i] = tmp
#         i = i+1
#         # swap
#         tmp = self.nums[i]
#         self.nums[i] = self.nums[end]
#         self.nums[end] = tmp
#         return i 

# # method_3
# #   快排写法2
# class Solution:
#     def sortArray(self, nums):
#         self.randomized_quicksort(nums, 0, len(nums)-1)
#         return nums

    
#     def randomized_quicksort(self,nums,start,end):
#         if start >= end:
#             return
#         pivot = self.randomized_partition(nums,start,end)
#         self.randomized_quicksort(nums,start,pivot-1)
#         self.randomized_quicksort(nums,pivot+1,end)
    
#     def randomized_partition(self,nums,start,end): 
#         pivot = random.randint(start,end) # random range [start,end]
#         nums[pivot],nums[end] = nums[pivot],nums[end]
#         i = start -1
#         for j in range(start,end):
#             if  nums[j] <= nums[end]:
#                 i += 1
#                 # swap
#                 nums[j], nums[i] = nums[i], nums[j]
#         i = i+1
#         # swap
#         nums[i], nums[end] = nums[end], nums[i]
#         return i