class Solution:
    def gameOfLife(self, board) -> None:
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


 

if __name__ == "__main__":
    s = Solution()
    print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))

