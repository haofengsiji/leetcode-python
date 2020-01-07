# import math
# class Solution(object):
#     '''
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         # Brute Force illustration:[https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-array.md]
#         # Time C: O(m+n) Space C: O(m+n)
#         new_nums = []
#         sorted_nums = []
#         new_nums = nums1 + nums2
#         l = len(new_nums)
#         i = 0 # Beginning of nums1
#         j = len(nums1) # Beginning of nums2
#         while True:
#             if i == len(nums1):
#                 sorted_nums += new_nums[j:] # add all left nums in nums2
#                 break
#             elif j == len(new_nums):
#                 sorted_nums += nums1[i:] # add all left nums in nums1
#                 break
#             else:
#                 if new_nums[i] <= new_nums[j]:
#                     sorted_nums.append(new_nums[i])
#                     i += 1
#                 else:
#                     sorted_nums.append(new_nums[j])
#                     j += 1
        
#         if l%2 == 0: # Even number
#             median = (sorted_nums[int(l/2-1)] + sorted_nums[int(l/2)])/2
#         else: # Odd number
#             median = sorted_nums[int((l-1)/2)]
        
#         return median
#     '''

#     # Binary Search illustration:[https://github.com/haofengsiji/leetcode-2/blob/master/problems/4.median-of-two-sorted-array.md]
#     # code reference from:[https://github.com/azl397985856/leetcode/blob/master/problems/4.median-of-two-sorted-array.md]
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         m = len(nums1)
#         n = len(nums2)
#         if m > n:
#             return self.findMedianSortedArrays(nums2,nums1)
#         lo = 0
#         hi = m
#         while lo <= hi:
#             i = int(lo + (hi - lo)/2)
#             j = int((m + n + 1)/2 - i)
#             max_left_nums1 = -math.inf if i == 0 else nums1[i-1]
#             min_right_nums1 = math.inf if i == m else nums1[i]
#             max_left_nums2 = -math.inf if j == 0 else nums2[j-1]
#             min_right_nums2 = math.inf if j == n else nums2[j]
            
#             if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
#                 if((m+n)%2 == 0):
#                     return float((max(max_left_nums1,max_left_nums2) + min(min_right_nums2,min_right_nums1))/2)
#                 else:
#                     return max(max_left_nums1,max_left_nums2)
#             elif max_left_nums1 > min_right_nums2:
#                 hi = i - 1
#             else:
#                 lo = i + 1
        
#         return 0.0


# # method 1: but use sorted() built-in function 
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums = nums1 + nums2
#         nums = sorted(nums)
#         n = len(nums)
#         if n%2 == 0:
#             med = (nums[n//2] + nums[n//2-1])/2
#         else:
#             med = nums[n//2]
#         return med

# method 2:
#   Binary search in nums1.
#   T:O(log(min(m,n)))
#   S:O(1)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2,nums1)
        hi = m
        lo = 0
        while lo <= hi:
            i = (hi + lo + 1)//2
            j = (m + n + 1)//2 - i
            left_nums1_max = -float('inf') if i == 0 else nums1[i-1]
            right_nums1_min = float('inf') if i == m else nums1[i]
            left_nums2_max = -float('inf') if j == 0 else nums2[j-1]
            right_nums2_min = float('inf') if j == n else nums2[j]
            if left_nums1_max <= right_nums2_min and left_nums2_max <= right_nums1_min:
                if (m+n)%2 == 0:
                    return (max(left_nums1_max,left_nums2_max) + min(right_nums1_min,right_nums2_min))/2
                else:
                    return max(left_nums1_max,left_nums2_max)
            elif left_nums1_max > right_nums2_min:
                hi = i - 1
            else:
                lo = i + 1
        return 0.0     

if __name__ == '__main__':

    # begin

    s = Solution()

    print(s.findMedianSortedArrays([1,2], [3,4,5]))


    