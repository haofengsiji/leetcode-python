# method_1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        ans = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if (s[i:j] == s[i:j][::-1]) & (j-i > len(ans)):
                    ans = s[i:j]
        return ans 

# # method_2
class Solution:
    def longestPalindrome(self, s):
        ans = ''
        n = len(s)
        dp = [[None]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i==j+1 or i==j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i-1][j+1]
                else:
                    dp[i][j] = False
                # update ans
                if dp[i][j] == True and i-j+1 > len(ans):
                    ans = s[j:i+1]
        return ans 

# # methode_3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
             # 偶数
            for l in range(min(i,len(s)-i)):
                if s[i - (l+1)] == s[i + l]:
                    ans = s[i-(l+1) : i+l + 1] if (l+1)*2 > len(ans) else ans
                else:
                    break
             # 奇数
            for l in range(min(i+1,len(s)-i)):
                if s[i - l] == s[i + l]:
                    ans = s[i-l: i+l + 1] if l*2+1 > len(ans) else ans
                else:
                    break
        return ans 

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r] 

if __name__ == "__main__":

    s = Solution()

    print(s.longestPalindrome('babad'))   