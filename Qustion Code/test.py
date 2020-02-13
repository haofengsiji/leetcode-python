class Solution:
    def trap(self, height) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # 当前高度大于栈顶，出栈
                h = stack.pop()
                # 出栈后为空，跳出
                if not stack:
                    break
                # 计算距离
                dis = i - stack[-1] -1
                # 计算深度 左高<-stack[-1] 右高 <-i, 弹出为当前
                deepth = min(height[stack[-1]],height[i]) - height[h]
                ans += dis*deepth
            stack.append(i)
        return ans


 

if __name__ == "__main__":
    s = Solution()
    print(s.trap([4,2,3]))

