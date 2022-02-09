import ttt.py

def X(square_num):
    board = make_empty_board()
    board[(square_num - 1) // 3][(square_num - 1) // 3] = "X"
    print_board_and_legend(board)