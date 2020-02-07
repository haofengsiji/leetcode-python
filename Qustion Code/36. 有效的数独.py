# method_1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        rowtable = {i:[] for i in range(row)}
        coltable = {i:[] for i in range(col)}
        squaretable = {(i,j):[] for i in range(3) for j in range(3)}
        for r in range(row):
            for c in range(col):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowtable[r]:
                    return False
                else:
                    rowtable[r].append(board[r][c])
                if board[r][c] in coltable[c]:
                    return False
                else:
                    coltable[c].append(board[r][c])
                if board[r][c] in squaretable[(r//3,c//3)]:
                    return False
                else:
                    squaretable[(r//3,c//3)].append(board[r][c])
        return True

# method_2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowtable = [{} for i in range(9)]
        coltable = [{} for i in range(9)]
        boxtable = [{} for i in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    num = int(num)
                    box_index = row//3*3+col//3

                    # 检查哈希表
                    rowtable[row][num] = rowtable[row].get(num,0) + 1
                    coltable[col][num] = coltable[col].get(num,0) + 1
                    boxtable[box_index][num] = boxtable[box_index].get(num,0) + 1

                    if rowtable[row][num] > 1 or coltable[col][num] > 1 or boxtable[box_index][num] >1:
                        return False
        return True
