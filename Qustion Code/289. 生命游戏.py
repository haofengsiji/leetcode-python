# method_1 遍历
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        # 遍历细胞
        for row in range(rows):
            for col in range(cols):
                
                count = 0 

                # 遍历邻居细胞
                for neighbor in neighbors:
                    cur_row = row + neighbor[0]
                    cur_col = col + neighbor[1]
                    # 1.有效位置 2.有细胞
                    if cur_row >= 0 and cur_row < rows and cur_col >= 0 and cur_col < cols \
                    and (board[cur_row][cur_col]  == 1 or board[cur_row][cur_col]  == -1):
                        count += 1
                
                # -1:过去活现在死；2:过去死现在活；0:一直死；1:一直活
                # 新规则1
                if board[row][col] == 1 and count < 2:
                    board[row][col] = -1
                # 新规则2
                elif board[row][col] == 1 and count >=2 and count <= 3:
                    board[row][col] = 1
                # 新规则3
                elif board[row][col] == 1 and count >3:
                    board[row][col] = -1
                # 新规则4
                elif board[row][col] == 0 and count == 3:
                    board[row][col] = 2
        # 更新细胞板
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

# method_2 卷积，没啥优势，了解一下卷积的写法
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        r,c=len(board),len(board[0])
        padding = 1
        #下面两行做zero padding
        board_exp=np.array([[0 for _ in range(c+2*padding)] for _ in range(r+2*padding)])
        board_exp[padding:padding+r,padding:padding+c]=np.array(board)
        #设置卷积核
        kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])
        #开始卷积
        for i in range(padding,r+padding):
            for j in range(padding,c+padding):
                #统计细胞周围8个位置的状态
                temp_sum=np.sum(kernel*board_exp[i-1:i+2,j-1:j+2])
                #按照题目规则进行判断
                if board_exp[i,j]==1:
                    if temp_sum<2 or temp_sum>3:
                        board[i-1][j-1]=0
                else:
                    if temp_sum==3:
                        board[i-1][j-1]=1
        return None           
