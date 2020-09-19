from typing import List
from collections import defaultdict 
import sys

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backTrace(board,i,j):
            if j == 9:
                return backTrace(board,i+1,0)
            if i == 9:
                return True
            if board[i][j] == '.':
                return backTrace(board,i,j+1)
            for num in range(1,1+9):
                if not isVaild(i,j,str(num)):
                    continue
                board[i][j] = str(num)
                if backTrace(board,i,j+1):
                    return True
                board[i][j] = '.'
            return False

            
        def isVaild(i,j,ch):
            for k in range(9):
                if board[i][k] == ch:
                    return False
                if board[k][j] == ch:
                    return False
                if board[(i//3)*3+k//3][(j//3)*3+k%3] == ch:
                    return False
            return True
        
        backTrace(board,0,0)
                
                    

if __name__ == "__main__":
    s = Solution()
    print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))