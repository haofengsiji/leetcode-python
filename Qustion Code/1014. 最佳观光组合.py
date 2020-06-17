# method_1
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        mx = 0
        for j in range(1,n):
            mx = max(A[j-1]+j-1,mx)
            ans = max(mx+A[j]-j,ans)
        return ans