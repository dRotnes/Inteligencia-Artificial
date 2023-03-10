from board import Board

FINAL_TABLE = []
BLANK_ROW_FINAL = 0
NUM_INVERSIONS_FINAL = 0
    

def checkIfSolution(board: Board):
    if board.getTable() == FINAL_TABLE:
        return True
    return False

def moveDown(board:Board):
    if(board.getBlankRow()<3):
        blank_row = board.getBlankRow()
        blank_col = board.getBlankCol()
        new_table = list(map(list, board.getTable())) 
        moveUp = new_table[blank_row + 1][blank_col]
        new_table[blank_row + 1][blank_col] = 0
        new_table[blank_row][blank_col] = moveUp

        new_board = Board(new_table, blank_row + 1, blank_col)
        return new_board
    return None

def moveUp(board:Board):
    if(board.getBlankRow()>0):
        blank_row = board.getBlankRow()
        blank_col = board.getBlankCol()
        new_table = list(map(list, board.getTable())) 
        moveUp = new_table[blank_row -1][blank_col]
        new_table[blank_row -1][blank_col] = 0
        new_table[blank_row][blank_col] = moveUp

        new_board = Board(new_table, blank_row -1, blank_col)
        return new_board
    return None

def moveRight(board:Board):
    if(board.getBlankCol()<3):
        blank_row = board.getBlankRow()
        blank_col = board.getBlankCol()
        new_table = list(map(list, board.getTable())) 
        moveUp = new_table[blank_row][blank_col+1]
        new_table[blank_row][blank_col+1] = 0
        new_table[blank_row][blank_col] = moveUp

        new_board = Board(new_table, blank_row, blank_col+1)
        return new_board
    return None

def moveLeft(board:Board):
    if(board.getBlankCol()>0):
        blank_row = board.getBlankRow()
        blank_col = board.getBlankCol()
        new_table = list(map(list, board.getTable())) 
        moveUp = new_table[blank_row][blank_col-1]
        new_table[blank_row][blank_col-1] = 0
        new_table[blank_row][blank_col] = moveUp

        new_board = Board(new_table, blank_row, blank_col-1)
        return new_board
    return None