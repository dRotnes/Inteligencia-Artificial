from board import Board
from shared import *

def __DFSLimRec(board: Board, path: list, depth:int, limit:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        return path, True
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)

    if(depth==limit):
        if(right is not None or left is not None or up is not None or down is not None):
            return None, False
        return None, True

    children = []
    end = True
    if(right is not None and right.getTable() not in path):
        children.append(right)
        
    if(left is not None and left.getTable() not in path):
        children.append(left)
    
    if(up is not None and up.getTable() not in path):
        children.append(up)
    
    if(down is not None and down.getTable() not in path):
        children.append(down)

    for child in children:
        result, rec_call_child = __DFSLimRec(child, list(map(list, path)), depth + 1, limit)
        if result is not None:
            return result, True
        end = end and rec_call_child
    return None, end

def __DFSLim(initial_board, limit):
    visited = []
    return __DFSLimRec(initial_board,visited,0, limit)

def IDFS(initial_board):
    limit = 0
    dfslim = False
    while not dfslim:
        result, dfslim = __DFSLim(initial_board, limit)
        if result is not None:
            print("---------- FOUND SOLUTION IN DEPTH " + str(limit) + " ----------\n")
            return result
        print("---------- NO SOLUTION FOUND IN LIMIT " + str(limit) + " ----------\n")
        limit+=1
    return None