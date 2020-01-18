# method_1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs or strs == []:
            return ''

        flag = True
        min_size = len(strs[0])
        for s in strs:
            min_size = min(len(s),min_size)

        for i in range(min_size):
            for j in range(1,len(strs)):
                if strs[j-1][i] == strs[j][i]:
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                break
            else:
                continue
                
        if flag == True:
            return strs[0][:min_size]
        else:
            return strs[0][:i]

# # method_2
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         s = ''
#         for i in zip(*strs):
#             if len(set(i)) == 1:
#                 s += i[0]
#             else:
#                 break
#         return s

# # method_3
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ''
#         prefix = strs[0]
#         for i in range(1,len(strs)):
#             while strs[i].find(prefix) != 0:
#                 prefix = prefix[0:-1]
            
#         return prefix
