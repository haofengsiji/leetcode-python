# method_1
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1],x[0]))
        ans = [pairs[0]]
        for i in range(1,len(pairs)):
            if ans[-1][-1] < pairs[i][0]:
                ans.append(pairs[i])
        return len(ans)