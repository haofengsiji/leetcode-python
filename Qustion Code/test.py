from collections import Counter
class Solution:
    def singleNumber(self, nums):
        hashmap = Counter(nums)
        for key in hashmap:
            if hashmap[key] == 1:
                return key


 

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))

