# method_1
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backTrack(board, i, j):
            # 穷举到最后一列，换到下一行开始
            if j == 9:
                return backTrack(board,i+1,0)
            
            # 穷举到最后一行，找到了 base case 结束递归
            if i == 9:
                return True

            # 有预设数字，直接跳过
            if board[i][j] != '.':
                return backTrack(board,i,j+1)
            
            # 从1到9穷举
            for num in range(1,9+1):
                # 遇到不合法的数字，跳过
                if not isValid(board,i,j,str(num)):
                    continue
                # 做选择
                board[i][j] = str(num)
                # 如果找到可行解，返回True
                if backTrack(board,i,j+1):
                    return True
                # 如果没有，撤销选择
                board[i][j] = '.'
            
            # 穷举完，依然无可行解，此路不通
            return False
            
        def isValid(board, r, c, ch):
            for k in range(9):
                # 检查列
                if board[r][k] == ch:
                    return False
                # 检查行
                if board[k][c] == ch:
                    return False
                # 检查方阵
                if board[(r//3)*3 + k//3][(c//3)*3 + k%3] == ch:
                    return False
            # 三种约束均无冲突
            return True
        
        backTrack(board,0,0)
        
        