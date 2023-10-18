import numpy as np

# 初始化棋盘
def init_board():
    board = np.zeros((15, 15), dtype=int)
    return board

# 打印棋盘
def print_board(board):
    print("  ", end="")
    for i in range(15):
        print(i, end=" ")
    print()
    for i in range(15):
        print(i, end=" ")
        for j in range(15):
            if board[i][j] == 0:
                print("+", end=" ")
            elif board[i][j] == 1:
                print("●", end=" ")
            else:
                print("○", end=" ")
        print()

# 判断是否结束
def is_over(board, row, col):
    # 判断行
    if col < 11:
        if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == board[row][col+4]:
            return True
    # 判断列
    if row < 11:
        if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == board[row+4][col]:
            return True
    # 判断右斜
    if row < 11 and col < 11:
        if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4]:
            return True
    # 判断左斜
    if row < 11 and col > 3:
        if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row+4][col-4]:
            return True
    return False

# 主函数
def main():
    # 初始化棋盘
    board = init_board()
    # 打印棋盘
    print_board(board)
    # 黑方先手
    player = 1
    while True:
        # 输入坐标
        print("请玩家%d输入坐标：" % player)
        row, col = input().split(",")
        row = int(row)
        col = int(col)
        # 判断是否可下
        if board[row][col] != 0:
            print("该位置已有棋子，请重新输入！")
            continue
        # 下子
        board[row][col] = player
        # 打印棋盘
        print_board(board)
        # 判断是否结束
        if is_over(board, row, col):
            print("恭喜玩家%d获胜！" % player)
            break
        # 切换玩家
        player = 3 - player

# 开始游戏
if __name__ == "__main__":
    main()
