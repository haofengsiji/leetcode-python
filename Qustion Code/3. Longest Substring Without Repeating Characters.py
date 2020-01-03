# Straightforwdrd method
#   1.Find max possible longest substring
#   2.loop all the possible substring
#   3.Use set() to judge unrepeating substring
#   T:O(n^2) S:O(k)
#       k is the size of set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxvoc = len(set(s))
        maxsub = 0
        for sub in range(1,maxvoc+1):
            for index in range(0,len(s)-sub+1):
                if len(set(s[index:index+sub])) == sub:
                    maxsub = sub
                    break
        return maxsub

# Sliding Window method
#   T:O(n) S:O(k)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        ans = 0
        max_ans = 0
        dic = {}
        for end,c in enumerate(s):
            if c in dic:    
                start = max(dic[c]+1,start) # skip the repeating character
            dic[c] = end
            ans = max(end - start + 1,ans)
        return ans
