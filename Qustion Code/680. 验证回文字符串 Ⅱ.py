# Method_1
class Solution:
    def validPalindrome(self, s: str) -> bool
        def checkPalindrome(i,j):
            while i < j:
                if s[i] == s[j]:
                    i += 1;
                    j -= 1;
                else:
                    return False
            return True
        
        low = 0
        high = len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                #return checkPalindrome(low+1,high) or checkPalindrome(low,high-1)
                return s[low+1:high+1] == s[low+1:high+1][::-1] or s[low:high-1+1] == s[low:high-1+1][::-1]
        return True