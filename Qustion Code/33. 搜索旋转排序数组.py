class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        if not nums: return -1
        while low < high-1:
            mid = (low+high)//2
            # 左边无旋转
            if nums[low] < nums[mid]:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid
                else:
                    low = mid
            # 右边无旋转
            else:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid
                else:
                    high = mid
        if nums[low] == target: return low
        if nums[high] == target: return high
        return -1