from board import Board
from shared import FINAL_TABLE, BLANK_ROW_FINAL, NUM_INVERSIONS_FINAL

def sumWrongPlacesHeuristics(board:Board):
    
    table = board.getTable()
    sum = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if(table[i][j] != FINAL_TABLE[i][j]):
                sum+=1
    return sum

def manhattanHeuristics(board:Board):

    table = board.getTable()
    sum = 0
    for i in range(len(table)):
        for j in range(len(table)):
            if(table[i][j] != FINAL_TABLE[i][j]):
                pos_in_final = [(index, row.index(table[i][j])) for index, row in enumerate(FINAL_TABLE) if table[i][j] in row][0]
                sum_dist = abs(pos_in_final[0] - i) + abs(pos_in_final[1] - j)
                sum+=sum_dist
    return sum

def chooseGetHeuristics(board:Board, heu:str):
    if(heu == "MAN"):
        return manhattanHeuristics(board)
    else:
        return sumWrongPlacesHeuristics(board)
