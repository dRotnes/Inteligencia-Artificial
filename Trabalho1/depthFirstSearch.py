from board import Board
from shared import checkIfSolution, moveUp, moveDown, moveLeft, moveRight

def __DFSRec(board: Board, path: list, depth:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        print("---------- FOUND SOLUTION IN DEPTH " + str(depth) + " ----------")
        for i in path:
            print(str(i) + " =>")
        return True
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)

    if(right is None and left is None and up is None and down is None):
        return False
    
    children = []
    if(right is not None and right.getTable() not in path):
        children.append(right)
        
    if(left is not None and left.getTable() not in path):
        children.append(left)

    if(up is not None and up.getTable() not in path):
        children.append(up)

    if(down is not None and down.getTable() not in path):
        children.append(down)

    for child in children:
        __DFSRec(child, list(map(list, path)), depth + 1)

def DFS(initial_board):
    visited = []
    return __DFSRec(initial_board,visited,0)
