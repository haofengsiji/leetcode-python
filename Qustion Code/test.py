class Solution:
    def findDuplicate(self, nums) -> int:
        right = len(nums)-1
        left = 1

        while left < right:
            mid = (left + right)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt > mid:
                right = mid
            else:
                left = mid + 1 
        return right


 

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1,3,4,5,2,2]))

