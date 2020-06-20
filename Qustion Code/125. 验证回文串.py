# method_1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.lower()
        while i < len(s):
            if s[i].isdigit() or s[i].isalpha():
                i += 1
            else:
                s = s[:i] + s[i+1:]

        return s == s[::-1]

# method_2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]