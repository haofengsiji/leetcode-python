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
    
        for substr in s_array:
            zigzag += substr
        
        return zigzag