import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")



def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    print("\n\n")

    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]

    print_board_and_legend(board)