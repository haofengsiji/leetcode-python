class Solution:
    def searchRange(self, nums, target: int):
        return [self.left_bound(nums,target),self.right_bound(nums,target)]


    def left_bound(self, nums,target):
        high = len(nums)
        low = 0
        # 中止条件[low,low)
        while low < high:
            mid = (low + high)//2
            if nums[mid] == target:
               high = mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return high if nums[high] == target else -1

    def right_bound(self, nums,target):
        high = len(nums)
        low = 0
        # 中止条件[low,low)
        while low < high:
            mid = (low + high)//2
            if nums[mid] == target:
                low = mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return low if nums[low] == target else -1 

if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8],8))

