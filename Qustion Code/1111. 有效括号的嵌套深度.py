# method_1 栈 平均分
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        d = 1
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d%2)
            if c == ')':
                ans.append(d%2)
                d -= 1
        return ans 


# method_2 规律
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == '(':
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
        return ans