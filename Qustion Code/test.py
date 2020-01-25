class Solution:
    def isValid(self, s: str) -> bool:
        dic = {']':'[','}':'{',')':'('}
        stack = []
        for c in s:
            if c in ['[','(','{']:
                stack.append(c)
            else:
                if stack and stack.pop() == dic[c]
                    continue
                else:
                    return False
        
        return True
            


        
                    

if __name__ == "__main__":
    s = Solution()

    print(s.isValid('()'))