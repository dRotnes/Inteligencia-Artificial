from board import Board
from shared import checkIfSolution, moveUp, moveDown, moveLeft, moveRight

def BFS(initial_board:Board):
    queue = []
    visited = []
    queue.append((initial_board, 0))
    num_nodes_gen = 0
    while(len(queue)!=0):
        current = queue.pop(0)
        visited.append(current[0].getTable())
        # print(current[0].getTable())
        if checkIfSolution(current[0]):
            return visited, current[1], num_nodes_gen
        
        right:Board = moveRight(current[0])
        left:Board = moveLeft(current[0])
        up:Board = moveUp(current[0])
        down:Board = moveDown(current[0])

        if(right is None and left is None and up is None and down is None):
            return None, None, None
        
        if(right is not None and right.getTable() not in visited):
            queue.append((right, current[1]+1)) 
            num_nodes_gen +=1

        if(left is not None and left.getTable() not in visited):
            queue.append((left,current[1]+1))
            num_nodes_gen +=1

        if(up is not None and up.getTable() not in visited):
            queue.append((up, current[1]+1))
            num_nodes_gen +=1

        if(down is not None and down.getTable() not in visited):
            queue.append((down, current[1]+1))
            num_nodes_gen +=1
