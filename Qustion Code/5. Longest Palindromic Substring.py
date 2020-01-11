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

# methode_3
    

if __name__ == "__main__":

    s = Solution()

    print(s.longestPalindrome('babad'))   