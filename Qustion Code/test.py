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




 

if __name__ == "__main__":
    s = Solution()
    print(s.multiply('13','2'))

