# method_1
class Solution:
    def romanToInt(self, s: str) -> int:
        Roma_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        out = 0
        for i,c in enumerate(s):
            if c in {'I','X','C'}:
                if len(s[i:])>= 2:
                    if Roma_dict[s[i+1]]//Roma_dict[c] == 5 \
                    or Roma_dict[s[i+1]]//Roma_dict[c]  == 10:
                        out -= Roma_dict[c]
                    else:
                        out += Roma_dict[c]
                else:
                    out += Roma_dict[c]
            else:
                out += Roma_dict[c]
        
        return out

# # method_2
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         Roma_dict={'I':1, 'IV':3,'V':5,'IX':8,'X':10,'XL':30,'L':50,'XC':80,'C':100,'CD':300,'D':500,'CM':800,'M':1000}
#         out = 0
#         for i,c in enumerate(s):
#             out = out + Roma_dict.get(s[max(i-1,0):i+1],Roma_dict[c])
#         return out