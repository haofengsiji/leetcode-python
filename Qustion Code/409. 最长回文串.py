# method_1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = collections.Counter(s)
        for key in cnt:
            ans += cnt[key]//2 * 2
        if ans < len(s):
            ans = ans+1
        return ans 