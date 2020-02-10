# method_1
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
 
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + 1

                width = dp[i][j]
                for i1 in range(i,-1,-1):
                    width = min(width,dp[i1][j])
                    curarea = width*(i-i1+1)
                    maxarea = max(maxarea,curarea)

        return maxarea

# method_2
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        if matrix == []: return 0
        
        dp = [0]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                # 计算每行的柱形图每列的值
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0

            # 计算柱形图最大面积
            maxarea = max(maxarea,self.histogram(dp))
        return maxarea
    
    def histogram(self,hights):
        maxarea = 0
        i_stack = [-1]

        for i in range(len(hights)):
            
            while i_stack != [-1] and hights[i] < hights[i_stack[-1]]:        
                maxarea = max(maxarea, hights[i_stack.pop()] * (i-i_stack[-1]-1))
            i_stack.append(i)
            
        while i_stack != [-1]:
            maxarea = max(maxarea, hights[i_stack.pop()] * (len(hights)-i_stack[-1]-1))
        
        return maxarea