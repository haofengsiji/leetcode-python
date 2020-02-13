# method_1 按行
class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []: return 0
        maxscan = max(height)
        length = len(height)
        count = 0
        for i in range(maxscan):
            if i != 0:
                for i1,h in enumerate(height):
                    height[i1] = 0 if h - 1 < 0 else h - 1
            layer_count = 0
            for start in range(length):
                if height[start] != 0:
                    break
            for end in range(length-1,-1,-1):
                if height[end] != 0:
                    break
            for j in range(start+1,end):
                if height[j] == 0:
                    layer_count +=1
            count += layer_count
        return count

# method_2 按列
class Solution:
    def trap(self, height) -> int:
        ans = 0
        for i in range(len(height)):
            leftmax = 0
            rightmax = 0
            # 找到左边最高
            for left in range(0,i):
                if height[left] > leftmax:
                    leftmax = height[left]

            # 找到右边最高
            for right in range(i+1,len(height)):
                if height[right] > rightmax:
                    rightmax = height[right]

            # 当前可以盛水的高度
            cur_height = min(rightmax,leftmax) - height[i]
            if cur_height > 0:
                ans += cur_height
        return ans

# method_3 dp辅助
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        ans = 0
        
        # 左边最高状态
        for i in range(1,n):
            left_max[i] = max(height[i-1],left_max[i-1])
        # 右边最高状态
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i+1],right_max[i+1])
        
        # 计算每列存储的水的高度
        for i in range(n):
            cur_height = min(left_max[i],right_max[i]) - height[i]
            if cur_height > 0:
                ans += cur_height
        return ans

# method_4 双指针 最巧妙左右一起更
class Solution:
    def trap(self, height) -> int:
        ans = 0
        for i in range(len(height)):
            leftmax = 0
            rightmax = 0
            # 找到左边最高
            for left in range(0,i):
                if height[left] > leftmax:
                    leftmax = height[left]

            # 找到右边最高
            for right in range(i+1,len(height)):
                if height[right] > rightmax:
                    rightmax = height[right]

            # 当前可以盛水的高度
            cur_height = min(rightmax,leftmax) - height[i]
            if cur_height > 0:
                ans += cur_height
        return ans

# 栈
class Solution:
    def trap(self, height: List[int]) -> int:
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