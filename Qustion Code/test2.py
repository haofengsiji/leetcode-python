from typing import List
def Binary_Search(nums:List[int],x:int):
    n = len(nums)
    # 上下边界
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

m=[1,2,3,4,8,9,11,12,18,19,20,28]
print(Binary_Search(m,14))