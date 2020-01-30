# method_1
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 1
        max_count = 0
        stack = []
        i_stack = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append([i,c])
            elif c == ')':
                if len(stack) == 0:
                    pass
                elif stack[-1][-1] == '(':
                    old_i,_ = stack.pop()
                    i_stack.append(old_i)
                    i_stack.append(i)
        i_stack.sort()
        for i in range(len(i_stack)-1):
            if i_stack[i]+1 == i_stack[i+1]:
                count +=1
                max_count = max(max_count,count)
            else:
                count = 1
        return max_count

# method_2
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        sub_pair = n//2
        max_len = 0
        for sp in range(1,sub_pair+1):
            for i in range(0,n-sp*2+1):
                stack = []
                flag = True
                for c in s[i:i+sp*2]:
                    if c == '(':
                        stack.append(c)
                    else:
                        if stack and stack.pop() == '(':
                            continue
                        else:
                            flag = False
                flag = flag and not stack
                if flag == True: max_len = max(max_len,sp*2)
        return max_len

# method_3
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_count = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # 不可能与之前的接上，重新设置起点
                    stack.append(i)
                else:
                    # 可能与开头接上
                    max_count = max(max_count,i-stack[-1])
        return max_count