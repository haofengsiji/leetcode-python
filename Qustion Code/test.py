class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        if len(a) < len(b):
            self.addBinary(b,a)
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        state = 0
        while i >= 0 or j >=0:
            # special case
            if j < 0:
                if carry == 1:
                    if a[i] == '1':
                        carry = 1
                        ans = '0' + ans
                        i -= 1
                    else:
                        carry = 0
                        ans = '1' + ans
                        i -= 1
                else:
                    ans = a[:i+1] + ans
                    break
            else:
                # accumulation
                if a[i] == '1':
                    state += 1
                if b[j] == '1':
                    state += 1
                if carry == 1:
                    state += 1
                    carry = 0
                # calculation
                if state == 0:
                    ans = '0' + ans 
                elif state == 1:
                    ans = '1' + ans 
                elif state == 2:
                    ans = '0' + ans 
                    carry = 1
                elif state == 3:
                    ans = '1' + ans 
                    carry = 1
                else:
                    assert "state error"
                # update loop state
                i -= 1
                j -= 1
                state = 0     
        if carry == 1:
            ans = '1' + ans
        return ans    


 

if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("101111","10"))

