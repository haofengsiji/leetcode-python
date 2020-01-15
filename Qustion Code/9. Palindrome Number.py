# method_1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

# # method_2
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 :
#             return False
#         rev = 0
#         x_copy = x
#         while(x_copy!=0):
#             pop = x_copy % 10
#             x_copy = x_copy//10
#             rev = rev*10 + pop
#         if rev == x:
#             return True
#         else:
#             return False