import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = collections.Counter(s)
        for key in cnt:
            ans += cnt[key]//2
        if ans < len(s):
            ans = ans+1
        return ans 


 

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))

