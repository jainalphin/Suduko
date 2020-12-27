import random
def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0

    # The range here is the amount
    # of numbers in the grid
    for i in range(9):
        # choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while (not CheckValid(Grid, row, col, num) or Grid[row][col] != 0):  # if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        Grid[row][col] = num;
    return Grid

def CheckValid(Grid, row, col, num):
    # check if in row
    valid = True
    # check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            # check if section is valid
            if (Grid[rowsection * 3 + x][colsection * 3 + y] == num):
                valid = False
    return valid

board = MakeSudoku()




def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_y = pos[1] // 3#y
    box_x = pos[0] // 3#x

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None
print()
print()
print("------------SUDUKO PROBLEM----------")
print()
print_board(board)
solve(board)
print()
print()
print("------------HERE IS SOLUITON----------")
print()
print_board(board)