import pprint
def findUnassignedLocation(sudokuBoard): # Returns the next empty spot, also returns a boolean that checks if it is solved.
    for row in xrange(9):
        for col in xrange(9):
            if sudokuBoard[row][col] == 0: return (False, row, col)
    return (True, None, None)

def noConflicts(sudokuBoard, row, col, num): # Checks if spot is safe
    return not usedInRow(sudokuBoard, row, num) and not usedInCol(sudokuBoard, col, num) and not usedInBox(sudokuBoard, row - (row % 3), col - (col%3), num)

def usedInRow(sudokuBoard, row, num): # Check if is in row
    if num in sudokuBoard[row]:
        return True
    return False

def usedInCol(sudokuBoard, col, num): # Check if is in column
    for row in xrange(9):
        if num == sudokuBoard[row][col]:
            return True
    return False

def usedInBox(sudokuBoard, boxStartRow, boxStartCol, num): # Check if is in box
    for row in xrange(3):
        for col in xrange(3):
            if sudokuBoard[row+boxStartRow][col+boxStartCol] == num:
                return True
    return False

def solve(sudokuBoard):
    solved, row, col = findUnassignedLocation(sudokuBoard)
    if solved:
        return True # Base Case
    for i in xrange(1,10):
        if noConflicts(sudokuBoard, row, col, i):
            sudokuBoard[row][col] = i

            if solve(sudokuBoard): return True
            sudokuBoard[row][col] = 0
    return False

def parse():
    line_ctr = 0
    board_ctr = 0
    data = []
    board = []
    row = []
    with open('sudoku.txt', 'rb') as f:
        for line in f:
            if not 'Grid' in line:
                row = [int(num) for num in line if num != '\n']
                board.append(row)
            if len(board) == 9:
                data.append(board)
                board = []
    return data

data = parse()
my_sum = 0


for board in data:
    solve(board)
    for x in xrange(3):
        if x == 0:
            my_sum += int(board[0][x])*100
        if x == 1:
            my_sum += int(board[0][x])*10
        if x == 2:
            my_sum += int(board[0][x])
print my_sum
