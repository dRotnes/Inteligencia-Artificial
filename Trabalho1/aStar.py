from heuristics import chooseGetHeuristics
from shared import checkIfSolution, moveDown, moveLeft, moveRight, moveUp
from board import Board

def __A_StarRec(frontier:list, visited:list, heuristic:str, num_nodes_gen:str):
    if(frontier):
        frontier.sort(key=lambda x: x[0])
        cur = frontier.pop(0)
        cur_board:Board = cur[1]
        cur_depth = cur[2]
        visited.append(cur_board.getTable())

        if checkIfSolution(cur_board):
            return visited, cur_depth, num_nodes_gen
        
        children = []
        right:Board = moveRight(cur_board)
        left:Board = moveLeft(cur_board)
        up:Board = moveUp(cur_board)
        down:Board = moveDown(cur_board)
        
        if(right is not None and right.getTable() not in visited):
            children.append(right)

        if(left is not None and left.getTable() not in visited):
            children.append(left)
        
        if(up is not None and up.getTable() not in visited):
            children.append(up)
        
        if(down is not None and down.getTable() not in visited):
            children.append(down)
        
        for child in children:
            num_nodes_gen += 1
            frontier.append((chooseGetHeuristics(child, heuristic), child, cur_depth+1))
        
        return __A_StarRec(frontier, visited, heuristic, num_nodes_gen)
    return None, None, num_nodes_gen

def A_star(initial_board:Board, heuristic:str):
    frontier = [(chooseGetHeuristics(initial_board, heuristic), initial_board, 0)]
    visited = []
    return __A_StarRec(frontier, visited, heuristic, 0)