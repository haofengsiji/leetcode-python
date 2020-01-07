class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        longest_str = s[0]
        max_count = 1
        # for each length
        for i in range(2,l+1):
            # for each string
            for j in range(l-i+1):
                temp = s[j:j+i]
                if temp == temp[::-1]:
                    if i > max_count:
                        max_count = i
                        longest_str = temp
                        break
        return longest_str

if __name__ == "__main__":

    s = Solution()

    print(s.longestPalindrome('babad'))   