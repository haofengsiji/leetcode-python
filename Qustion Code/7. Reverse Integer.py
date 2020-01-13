# method_1
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        x = str(abs(x))
        x = x[::-1]
        x = int(x)
        if sign*x >= -2**31 and sign*x <= 2**31-1:
            return sign*x
        else:
            return 0