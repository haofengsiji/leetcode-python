# method_1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        ans = []
        cur_s = ''

        def generateTree(s,l_n,r_n):
            # 情况1：匹配完全，记录此答案
            if l_n == 0 and r_n == 0:
                ans.append(s)
                return
            # 情况2：左括号多于右括号，说明s中有多余的右括号，剪枝
            if l_n > r_n:
                return
            # 生成左右分支
            if l_n > 0:
                generateTree(s + '(',l_n-1,r_n)
            if r_n > 0:
                generateTree(s + ')',l_n,r_n-1)

        
        generateTree(cur_s,n,n)
        return ans

# # method_2
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # 状态初始化（特殊情况）
#         dp = [None for _ in range(n+1)]
#         dp[0] = ['']
#         dp[1] = ['()']
#         cur_s = []

#         # 状态转移
#         for i in range(2,n+1):
#             for j in range(0,i):

#                 for s1 in dp[j]:
#                     for s2 in dp[i-1-j]:
#                         cur_s.append('('+s1+')'+s2)
                        
#             dp[i] = cur_s
#             cur_s = []
#         return dp[n]