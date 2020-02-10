# method_1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxarea = 0

        for i in range(len(heights)):

            # 如果柱形图是递增的，push到stack，如果不是，计算可能的面积    
            while stack != [-1] and heights[i] < heights[stack[-1]]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack != [-1]:
            maxarea = max(maxarea,heights[stack.pop()] * (len(heights)- stack[-1] - 1))
        
        return maxarea