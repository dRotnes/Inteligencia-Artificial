from board import Board
from shared import checkIfSolution, moveUp, moveDown, moveLeft, moveRight

def __DFSRec(board: Board, path: list, depth:int, num_nodes_gen:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        print("---------- FOUND SOLUTION IN DEPTH " + str(depth) + " ----------")
        return path, num_nodes_gen
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)
    
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
        num_nodes_gen+=1
        dfsRec, n_nodes = __DFSRec(child, list(map(list, path)), depth + 1, num_nodes_gen)
        if dfsRec is not None:
            return dfsRec, n_nodes
    return None, None

def DFS(initial_board):
    visited = []
    try:
        result, num_nodes_gen= __DFSRec(initial_board,visited,0, 1)
        if result is not None:
            return result, num_nodes_gen 
        else:
            print("NO SOLUTION FOUND ON DFS")
    except:
        print("DFS REACHED MAXIMUM RECURSION DEPTH, NO SOLUTION FOUND\n")
        return None, None

