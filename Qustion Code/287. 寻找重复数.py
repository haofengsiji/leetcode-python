# method_1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
# method_2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow