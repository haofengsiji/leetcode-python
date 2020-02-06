# method_1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 1 and nums[0] == target: return [0,0]
        high = n-1
        low = 0
        i = -1
        while low < high:
            mid = (low + high)//2
            if target >= nums[low] and target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
            if nums[low] == target:
                i = low
                break
            elif nums[high] == target:
                i = high
                break
        j = i
        if i == -1:
            return [-1,-1]
        while i < n and nums[i] == target:
            i = i+1
        while j > -1 and nums[j] == target:
            j = j-1
        return [j+1,i-1]

# method_2
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.left_bound(nums,target),self.right_bound(nums,target)]

    def left_bound(self, nums,target):
        high = len(nums)-1
        if high == -1: return -1
        low = 0
        while low < high:
            mid = (low+high)//2
            if nums[mid] == target:
                high = mid
            elif nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1
        return high if nums[high] == target else -1
    
    def right_bound(self,nums,target):
        high = len(nums)
        if high == 0: return -1
        low = 0
        while low < high:
            mid = (high+low)//2
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid
        return low-1 if nums[low-1] == target else -1