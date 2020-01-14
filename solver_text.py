#----------------------------------------
#solver_text.py
#Author: akrobbin93
#----------------------------------------


#----------------------------------------
#imports
#----------------------------------------
import pprint


def solve(board):
#----------------------------------------
#solves a sudoku board via backtracking
#param board: 2d list of ints
#returns: solution
#----------------------------------------
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True
    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board, position, num):
#----------------------------------------
#determines if the attempted move is a valid one
#param board: 2d list of ints
#param position: (row, col)
#param num: int
#return: bool
#----------------------------------------

    #Check the row
    for i in range(0, len(board)):
        if board[position[0]][i] == num and position[1] != i:
            return False

    #Check the row
    for i in range(0, len(board)):
        if board[i][position[1]] == num and position[1] != i:
            return False

    #Check the box
    box_x = position[1]//3
    box_y = position[0]//3

    for i in range(box_y*3, box_x*3 + 3):
        for j in range(box_x*3, box_y*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True

def find_empty(board):
#----------------------------------------
#finds an open space on the board to try to fill
#param board: 2d list of ints
#return: row, col as (int,int)
#----------------------------------------

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
#----------------------------------------
#finds an open space on the board to try to fill
#param board: 2d list of ints
#return: None
#----------------------------------------

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ")

test_board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]

]

pp = pprint.PrettyPrinter(width=41)
solve(test_board)
pp.pprint(test_board)
