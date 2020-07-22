# method_1
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high)//2
            if numbers[mid] < numbers[high]:
                high = mid
            elif numbers[mid] > numbers[high]:
                low = mid + 1
            else:
                high -= 1

        return numbers[low]
            
