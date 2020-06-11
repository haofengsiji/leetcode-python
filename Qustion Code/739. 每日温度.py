# method_1
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = dict()
        ans = [0]*len(T)
        big = float('inf')
        for i in range(len(T)-1,-1,-1):
            warmer_index = min(nxt.get(t,big) for t in range(T[i]+1,102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans

# method_2
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(T)
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans