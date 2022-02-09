

    if y_end + d_y > len(board) or x_end + d_x > len(board):
        return "CLOSED"
    elif y_end + d_y <= len(board) and x_end + d_x <= len(board):
        if board[y_end+d_y][x_end+d_x] != " " and board[y_end-length*d_y][x_end-length*d_x] != " ":
            return "CLOSED"
        elif board[y_end+d_y][x_end+d_x] == " " and board[y_end-length*d_y][x_end-length*d_x] == " ":
            return "OPEN"
        else:
            return "SEMI-OPEN"
    elif y_end + d_y <= len(board) and x_end + d_x > len(board):
        if board[y_end-length*d_y][x_end-length*d_x] != " ":
            return "CLOSED"
        else:
            return "SEMI-OPEN"
    elif y_end + d_y > len(board) and x_end + d_x <= len(board):
        if board[y_end-length*d_y][x_end-length*d_x] != " ":
            return "CLOSED"
        else:
            return "SEMI-OPEN"






    # open_b = {}
    # semi_open_b = {}
    # open_w = {}
    # semi_open_w = {}
    #
    # for i in range(2, 6):
    #     open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
    #     open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
    #
    # print(open_b)

    d = [(0,1), (1,0), (1,1), (1,-1)]

    for y_start in range(len(board)):
        for x_start in range(len(board[y_start])):
            R = [board[y_start][x_start]]
            for (d_y, d_x) in d:
                y = d_y
                x = d_x
                if d_y + d_x > 1:
                    for i in range((min(len(board)-y_start, len(board)-x_start))-1):
                        print(y_start, d_y, x_start, d_x)
                        R.append(board[y_start + d_y][x_start + d_x])
                        d_y += y
                        d_x += x
                elif d_y + d_x == 0:
                    for i in range((min(len(board)-y_start, x_start + 1))-1):
                        R.append(board[y_start + d_y][x_start + d_x])
                        d_y += y
                        d_x += x
                else:
                    for i in range(len(board)-1):
                        R.append(board[y_start + d_y][x_start + d_x])
                        d_y += y
                        d_x += x
    print(R)











    # for i in range(8):
    #     put_seq_on_board(board, 0,i,1,0,8,"w")
    # put_seq_on_board(board, 0,1,1,0,4,"b")
    # put_seq_on_board(board, 1,1,1,1,5,"w")
    # board[0][5] = "w"
    # board[0][6] = "b"
    # y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    # y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    # put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    # y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    # put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    # print_board(board)

    # board = make_empty_board(8)
    # board[2][2] = "w"
    # y = 3;
    # x = 2;
    # d_x = 0;
    # d_y = 1;
    # length = 5
    # put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    # print_board(board)




    if d_y == 1 and d_x == -1:





        if y_end - length >= 0 and x_end + length <= min(x_end + 1, len(board) - x_end):
            if board[y_end - length][x_end + length] == " ":
                if y_end + 1 <= x_end - 1 and x_end - 1 >= 0:
                    if board [y_end + 1][x_end - 1] == " ":
                        return "OPEN"
                    else:
                        return "SEMI-OPEN"
                else:
                    return "SEMI-OPEN"
            elif board[y_end - length][x_end + length] != " ":
                if y_end + 1 <= x_end - 1 and x_end - 1 >= 0:
                    if board [y_end + 1][x_end - 1] != " ":
                        return "CLOSED"
                    else:
                        return "SEMI-OPEN"
                elif y_end == 0 or x_end == 0:
                    return "CLOSED"
                else:
                    return "SEMI-OPEN"
                # if y_end + 1 and x_end - 1
        else:
            if y_end + 1 <= x_end - 1 and x_end - 1 >= 0:
                if board [y_end + 1][x_end - 1] == " ":
                    return "SEMI-OPEN"
                else:
                    return "CLOSED"
            elif board[y_end - length][x_end + length] != " ":
                if y_end + 1 <= x_end - 1 and x_end - 1 >= 0:
                    if board [y_end + 1][x_end - 1] != " ":
                        return "CLOSED"
                    else:
                        return "SEMI-OPEN"
                elif y_end == 0 or x_end == 0:
                    return "CLOSED"
                else:
                    return "SEMI-OPEN"
            else:

    list_of_keys = list(d.keys())
    list_of_items = list(d.items())
    l = []
    for i in range(len(list_of_keys)):
        l.append(list_of_keys[i])
        l.append(list_of_items[i])









































