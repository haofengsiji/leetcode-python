# method_1
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.combine(letter_dic[digits[0]],'')

        return self.combine(letter_dic[digits[0]],self.letterCombinations(digits[1:]))
        
    def combine(self,a,b):
        com = []

        if b == '':
            for c1 in a:
                com.append(c1)
        else:
            for c1 in a:
                for c2 in b:
                    com.append(c1+c2)
        return com

# # method_2
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         phone = {'2':['a','b','c'],
#                         '3':['d','e','f'],
#                         '4':['g','h','i'],
#                         '5':['j','k','l'],
#                         '6':['m','n','o'],
#                         '7':['p','q','r','s'],
#                         '8':['t','u','v'],
#                         '9':['w','x','y','z']}
        
#         def trace(comb,next_digits):
#             # 拆完了
#             if not next_digits:
#                 output.append(comb)
#             # 没拆完
#             else:
#                 for i in phone[next_digits[0]]:
#                     trace(comb+i,next_digits[1:])
        
#         output = []
#         if digits:
#             trace('',digits)
#         return output
        