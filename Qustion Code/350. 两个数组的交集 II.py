# method_1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.intersect(nums2,nums1)
        mp = dict()
        for num in nums1:
            mp[num] = mp.get(num,0) + 1
        res = []
        for num in nums2:
            if num in mp:
                mp[num] -= 1
                if mp[num] >= 0:
                    res.append(num)
                else:
                    mp.pop(num)
        
        return res

# method_2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res

# method_3
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return list(num.elements())