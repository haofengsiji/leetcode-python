# method_1
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0]*(m+n)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                # 当前位相乘结果
                mul = (ord(num1[j]) - ord('0'))*(ord(num2[i]) - ord('0'))
                # 当前低位指针，高位指针
                p1,p2 = i+j,i+j+1
                # 当前低位高位求和
                mul += res[p2]
                res[p2] = mul % 10
                res[p1] += mul // 10 
        i = 0
        while res != [] and res[0] == 0:
            res.pop(0)
        ans = ''
        for i in range(len(res)):
            ans += chr(res[i]+ord('0'))
        if len(ans) == 0:
            ans = '0'
        return ans 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                mul = (ord(num1[j]) - ord('0'))*(ord(num2[i]) - ord('0'))*(10**(m+n-2-i-j))
                res += mul
        return str(res)
