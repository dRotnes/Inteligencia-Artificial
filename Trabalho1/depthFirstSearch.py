from board import Board
from shared import checkIfSolution, moveUp, moveDown, moveLeft, moveRight

def __DFSRec(board: Board, path: list, depth:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        print("---------- FOUND SOLUTION IN DEPTH " + str(depth) + " ----------")
        return path
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)

    if(right is None and left is None and up is None and down is None):
        return None
    
    children = []
    
    if(right is not None and right.getTable() not in path):
        children.append(right)
    
    if(down is not None and down.getTable() not in path):
        children.append(down)
        
    if(left is not None and left.getTable() not in path):
        children.append(left)

    if(up is not None and up.getTable() not in path):
        children.append(up)

    for child in children:
        dfsRec = __DFSRec(child, list(map(list, path)), depth + 1)
        if dfsRec is not None:
            return dfsRec
    return None

def DFS(initial_board):
    visited = []
    try:
        result = __DFSRec(initial_board,visited,0)
        if result is not None:
            return result
        else:
            print("NO SOLUTION FOUND ON DFS")
    except:
        print("DFS REACHED MAXIMUM RECURSION DEPTH, NO SOLUTION FOUND\n")
        return None

