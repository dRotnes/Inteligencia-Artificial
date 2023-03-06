class Board:
    def __init__(self, table, blank_row, blank_col):
        self.table = table
        self.blank_row = blank_row
        self.blank_col = blank_col

    def getTable(self):
        return self.table
    
    def getBlankRow(self):
        return self.blank_row
    
    def getBlankCol(self):
        return self.blank_col
    
def testSolvability(blank_row, num_inversions):
    if(blank_row%2 != 0 and num_inversions%2 != 0):
        return True
    
    elif(blank_row%2 == 0 and num_inversions%2 == 0):
        return True
    
    else:
        return False
        
    
    
def checkIfSolution(board: Board):
    last_num = -1
    table = board.getTable()
    if(table[len(table)-1][len(table)-1] == 0):
        for i in table:
            for j in i:
                if(last_num>j and j!=0):
                    return False
                last_num = j
        return True
    return False

def getStringTable(table):
    string_matrix = ""
    for i in table:
        for j in i:
            string_matrix += str(j)
    return string_matrix

def moveDown(board:Board):
    if(board.getBlankRow() + 1 <=3):
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
    if(board.getBlankRow() - 1 >=0):
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
    if(board.getBlankCol() + 1 <=3):
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
    if(board.getBlankCol() - 1 >=0):
        blank_row = board.getBlankRow()
        blank_col = board.getBlankCol()
        new_table = list(map(list, board.getTable())) 
        moveUp = new_table[blank_row][blank_col-1]
        new_table[blank_row][blank_col-1] = 0
        new_table[blank_row][blank_col] = moveUp

        new_board = Board(new_table, blank_row, blank_col-1)
        return new_board
    return None

def DFSLimRec(board: Board, path: list, depth:int, limit:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        print("---------- FOUND SOLUTION ----------")
        for i in path:
            print(str(i), " => ")
        print("---------- END OF SOLUTION ----------\n")
        return True
    if(depth<limit):
        right:Board = moveRight(board)
        left:Board = moveLeft(board)
        up:Board = moveUp(board)
        down:Board = moveDown(board)
        dfs_right = False
        dfs_left = False
        dfs_up = False
        dfs_down = False

        if(right is not None and right.getTable() not in path):
            dfs_right = DFSLimRec(right, list(map(list, path)), depth + 1, limit)
        
        if(left is not None and left.getTable() not in path):
            dfs_left = DFSLimRec(left, list(map(list, path)), depth + 1, limit)
        
        if(up is not None and up.getTable() not in path):
            dfs_up = DFSLimRec(up, list(map(list, path)), depth + 1, limit)
        
        if(down is not None and down.getTable() not in path):
            dfs_down = DFSLimRec(down, list(map(list, path)), depth + 1, limit)

        return dfs_right or dfs_left or dfs_up or dfs_down

def DFSLim(initial_board, limit):
    visited = []
    return DFSLimRec(initial_board,visited,0, limit)

def IDFS(initial_board):
    limit = 0
    while(True):
        dfslim = DFSLim(initial_board, limit)
        if(dfslim):
            print("FOUND IN LIMIT " + str(limit))
            return
        print("NOT FOUND IN LIMIT " + str(limit))
        limit+=1

initial_table = []
t = []
blank_row = 0
blank_col = 0

with open("config.txt") as fileIn:
    for line in fileIn:
        t = list(map(int, line.split()))

while t != []:
    initial_table.append(t[:4])
    t = t[4:]

num_inversions = 0
last_num = -1
for i in range(len(initial_table)):
    for j in range(len(initial_table)):
        if(last_num>initial_table[i][j] and initial_table[i][j]!=0 and last_num!=0):
            num_inversions+=1
        if(initial_table[i][j] == 0):
            blank_row = i
            blank_col = j
        last_num = initial_table[i][j]

if(testSolvability(blank_row + 1,num_inversions)):
    initial_board = Board(initial_table, blank_row, blank_col)
    IDFS(initial_board)
else:
    print("Unsolvable Board")


