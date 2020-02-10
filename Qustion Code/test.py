class Solution:
    def test(self, matrix):
        maxarea = 0
        if len(matrix) == 0: return 0
        
        dp = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                # 计算当前行柱状图
                dp[j] = dp[j]+1 if matrix[i][j] == '1' else 0
            
            # 计算当前行柱状图的最大面积,leetcode84
            maxarea = max(maxarea,self.MaxArea(dp))
        
        return maxarea

    def MaxArea(self,hights):
        stack = [-1]
        maxarea = 0

        for i in range(len(hights)):
            if stack[-1] == -1:
                stack.append(i)
            elif hights[i] >= hights[stack[-1]]:
                stack.append(i)
            else:
                while hights[i] < hights[stack[-1]] and stack[-1] != -1:
                    index = stack.pop()
                    hight = hights[index]
                    width = i - index
                    maxarea = max(maxarea,width*hight)
                stack.append(i)
        
        while stack[-1] != -1:
            index = stack.pop()
            hight = hights[index]
            width = index - stack[-1] if hight != hights[stack[-1]] else index - stack[-1] + 1
            maxarea = max(maxarea,width*hight)
        return maxarea


 

if __name__ == "__main__":
    s = Solution()
    print(s.test([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

