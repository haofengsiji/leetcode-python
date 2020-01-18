# method_1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_cap = 0 
        i = 0
        j = len(height)-1
        while i !=j:
            max_cap = max(max_cap, (j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_cap

# # method_2 (out of time)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_cap = 0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 cap = (j-i)*min(height[i],height[j])
#                 max_cap = max(max_cap,cap)
#         return max_cap