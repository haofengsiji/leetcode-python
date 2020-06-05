# method_1
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []: return []
        low = 0
        high = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        ans = []

        while True:
            # →
            for i in range(left,right+1):
                ans.append(matrix[low][i])
            low += 1
            if low > high:
                break
            # ↓
            for i in range(low,high+1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            # ←
            for i in range(right,left-1,-1):
                ans.append(matrix[high][i])
            high -= 1
            if high < low:
                break
            # ↑
            for i in range(high,low-1,-1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ans

# method_2
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

