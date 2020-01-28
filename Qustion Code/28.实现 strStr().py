# method_1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_h = len(haystack)
        n_n = len(needle)
        if n_n == '': return 0
        for i in range(n_h-n_n+1):
            if haystack[i:i+n_n] == needle:
                return i
        return -1

# method_2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)