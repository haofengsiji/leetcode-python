# method_1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        s_array = ['' for _ in range(numRows)]
        zigzag = ''
        for i,c in enumerate(s):
            i = i % ((numRows-1)*2)
            if i < numRows:
                s_array[i] += c
            else:
                i = (numRows-1)*2 - i
                s_array[i] += c
        
        return "".join(s_array)

# # method_2
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2:
#             return s
#         i,flag = 0,-1
#         s_array = ["" for _ in range(numRows)]
#         for c in s:
#             s_array[i] += c
#             if i == 0 or i == numRows - 1: flag = -flag
#             i += flag
        
#         return "".join(s_array)