# method 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{:b}'.format(int(a,2)+int(b,2))

# method 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        carry = 0
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a[-1])
                a.pop()
            if b:
                carry += int(b[-1])
                b.pop()
            
            ans = str(carry %2) + ans
            carry = carry//2
        
        return ans

# method 3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        while y:
            ans = x^y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]