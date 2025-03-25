def solution(board):
    route = [-1,0,1]
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                for i in route:
                    for j in route:
                        if i == 0 and j == 0: continue
                        if x + i >= 0 and x + i < len(board):
                            t_x = x + i
                        elif x + i < 0: t_x = 0
                        elif x + i >= len(board): t_x = len(board) - 1
                        if y + j >= 0 and y + j < len(board):
                            t_y = y + j 
                        elif y + j < 0: t_y = 0
                        elif y + j >= len(board): t_y = len(board) - 1
                        # print(f'x: {x}, y: {y}, i: {i}, j: {j}, x+i: {x+i}, y+j: {y+j}, t_x: {t_x}, t_y: {t_y}')
                        if board[t_x][t_y] == 0:
                            board[t_x][t_y] = 2
    answer = 0
    for c in board:
        answer += c.count(0)
    return answer