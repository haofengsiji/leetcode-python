class Solution:
    def isValid(self, s: str) -> bool:
        dic = {']':'[','}':'{',')':'('}
        stack = []
        for c in s:
            if c in ['[','(','{']:
                stack.append(c)
            else:
                # 非空，有的匹配
                if stack and stack.pop() == dic[c]:
                    continue
                else:
                    return False
        # stack 必须是空，才说明匹配完全
        return True and not stack