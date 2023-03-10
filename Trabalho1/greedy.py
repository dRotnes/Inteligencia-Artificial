from heuristics import chooseGetHeuristics
from shared import checkIfSolution, moveDown, moveLeft, moveRight, moveUp
from board import Board

def __greedyRec(board:Board, visited:list, heuristic:str, depth:int, num_nodes_gen:int):
    visited.append(board.getTable())
    if(checkIfSolution(board)):
        return visited, depth, num_nodes_gen
    
    right:Board = moveRight(board)
    left:Board = moveLeft(board)
    up:Board = moveUp(board)
    down:Board = moveDown(board)
    
    children = []
        
    if(right is not None and right.getTable() not in visited):
        children.append((right, chooseGetHeuristics(right, heuristic)))
        num_nodes_gen+=1

    if(left is not None and left.getTable() not in visited):
        children.append((left, chooseGetHeuristics(left, heuristic)))
        num_nodes_gen+=1
    
    if(up is not None and up.getTable() not in visited):
        children.append((up, chooseGetHeuristics(up, heuristic)))
        num_nodes_gen+=1
    
    if(down is not None and down.getTable() not in visited):
        children.append((down, chooseGetHeuristics(down, heuristic)))
        num_nodes_gen+=1
    
    if(len(children)>0):
        children.sort(key=lambda x: x[1])
        return __greedyRec(children.pop(0)[0], visited, heuristic, depth+1, num_nodes_gen)
    return None, None, num_nodes_gen

def greedy(initial_board:Board, heuristic:str):
    visited = []
    return __greedyRec(initial_board, visited, heuristic, 0, 0)
