from board import Board
from shared import checkIfSolution, moveUp, moveDown, moveLeft, moveRight

def __DFSRec(board: Board, path: list, depth:int, num_nodes_gen:int):
    # print(board.getBoard())
    path.append(board.getTable())
    if(checkIfSolution(board)):
        return path, num_nodes_gen, str(depth)
    
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
        dfsRec, n_nodes, depthRec = __DFSRec(child, path, depth + 1, num_nodes_gen)
        if dfsRec is not None:
            return dfsRec, n_nodes, depthRec
    return None, None, None

def DFS(initial_board):
    visited = []
    try:
        result, num_nodes_gen, depth = __DFSRec(initial_board,visited,0, 1)
        return result, num_nodes_gen , depth
    except:
        print("MAXIMUM RECURSION DEPTH EXCEEDED\n")
        return None, None, None

