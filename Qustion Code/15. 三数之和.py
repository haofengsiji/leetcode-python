# method_1
class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i,num in enumerate(nums[:-2]):
            # 判断头部是否重复
            if i > 0 and num == nums[i-1]:
                continue
            two = self.twoSum(-num,nums[i+1:])
            if two != []:
                for t in two:
                    ans.append([num]+t)
        return ans

    
    def twoSum(self,target,nums):
        hash_table = {}
        ans = []
        for i,num in enumerate(nums):
            if target - num in hash_table:
                # 判断是否重复
                if [target-num,num] not in ans:
                    ans.append([target-num,num])
            hash_table[num] = i
        return ans

# # method_2
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         n = len(nums)
#         ans = []
#         for i in range(n):
#             if i>0 and nums[i] == nums[i-1]:
#                 continue
#             L = i+1
#             R = n-1
#             while L < R:
#                 s = nums[i] + nums[L] + nums[R]
#                 if s == 0:
#                     ans.append([nums[i],nums[L],nums[R]])
#                     L += 1
#                     R -= 1
#                     while (L < R and nums[L] == nums[L-1]):
#                             L += 1
#                     while (L < R == nums[R] == nums[R+1]):
#                             R -= 1
#                 elif s > 0:
#                     R -= 1
#                 else:
#                     L +=1            
#         return ans
