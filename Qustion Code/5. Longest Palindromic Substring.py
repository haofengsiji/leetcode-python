# method_1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        longest_str = s[0]
        max_count = 1
        # for each length
        for i in range(2,l+1):
            # for each string
            for j in range(l-i+1):
                temp = s[j:j+i]
                if temp == temp[::-1]:
                    if i > max_count:
                        max_count = i
                        longest_str = temp
                        break
        return longest_str

# # method_2
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         # initialization
#         size = len(s)
#         max_count = 0
#         ri = 0
#         rj = 0
#         dp = [[False for _ in range(size)] for _ in range(size)]

#         #dp process
#         for j in range(size):
#             for i in range(0,j+1):
#                 # assign status
#                 if i == j:
#                     dp[i][j] = True
#                 elif s[i] == s[j]:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#                 # max judgement
#                 if dp[i][j] == True and j-i+1 > max_count:
#                     ri = i
#                     rj = j
#                     max_count = j-i+1
        
#         return s[ri:rj+1]

# # methode_3
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         size = len(s)
#         ri = 0
#         rj = 0
#         max_count = 0 
#         if size == 0:
#             return s

#         # even substr
#         for i in range(size-1):
#             for j in range(min(i+1,size-(i+1))):
#                 if s[i-j] == s[i+1+j]:
#                     if 2*(j+1) > max_count:
#                         ri = i
#                         rj = j 
#                         max_count = 2*(j+1)
#                         flag = True       
#                 else:
#                     break
        
        
#         # odd substr
#         for i in range(size):
#             for j in range(min(i+1,size-(i+1)+1)):
#                 if s[i-j] == s[i+j]:
#                     if 2*j+1 > max_count:
#                         ri = i
#                         rj = j 
#                         max_count = 2*j+1
#                         flag = False
#                 else:
#                     break
        
#         if flag == True:
#             return s[ri-rj:(ri+1+rj)+1]
#         else:
#             return s[ri-rj:(ri+rj)+1]   

if __name__ == "__main__":

    s = Solution()

    print(s.longestPalindrome('babad'))   