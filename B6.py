# https://programmers.co.kr/learn/courses/30/lessons/17679
# 프렌즈4블록

BLANK_BLOCK = ' '
def delete_block(m, n, board):
    result = 0
    next_board = [board[i][0:n] for i in range(m)]

    for i in range(m - 1):
        for j in range(n - 1):
            temp = board[i][j]
            if temp != BLANK_BLOCK \
                    and temp == board[i + 1][j] \
                    and temp == board[i][j + 1] \
                    and temp == board[i + 1][j + 1]:
                if next_board[i][j] != BLANK_BLOCK:
                    next_board[i] = next_board[i][0:j] + BLANK_BLOCK + next_board[i][j + 1:n]
                    result += 1
                if next_board[i + 1][j] != BLANK_BLOCK:
                    next_board[i + 1] = next_board[i + 1][0:j] + BLANK_BLOCK + next_board[i + 1][j + 1:n]
                    result += 1
                if next_board[i][j + 1] != BLANK_BLOCK:
                    next_board[i] = next_board[i][0:j + 1] + BLANK_BLOCK + next_board[i][j + 2:n]
                    result += 1
                if next_board[i + 1][j + 1] != BLANK_BLOCK:
                    next_board[i + 1] = next_board[i + 1][0:j + 1] + BLANK_BLOCK + next_board[i + 1][j + 2:n]
                    result += 1

    return result, next_board

def move_down_block(m, n, board) -> bool:
    flag = False
    for i in range(m - 2, -1, -1):
        for j in range(n):
            if board[i][j] == BLANK_BLOCK and board[i + 1][j] != BLANK_BLOCK:
                flag = True
                board[i] = board[i][0:j] + board[i + 1][j] + board[i][j + 1:n]
                board[i + 1] = board[i + 1][0:j] + BLANK_BLOCK + board[i + 1][j + 1:n]
                
    return flag

def solution(m, n, board):
    answer = 0
    board = board[::-1]
    
    while True:
        temp, board = delete_block(m, n, board)
        if temp == 0:
            break
        answer += temp
        while(move_down_block(m, n, board) == True):
            pass
        
    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))