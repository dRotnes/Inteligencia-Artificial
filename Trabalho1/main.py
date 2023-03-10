from board import Board
from shared import FINAL_TABLE, BLANK_ROW_FINAL, NUM_INVERSIONS_FINAL
from depthFirstSearch import DFS
from iterativeDepthFirstSearch import IDFS
from breadthFirstSearch import BFS
from aStar import A_star

def testSolvability(blank_row, num_inversions):
    return (num_inversions%2 == 0) == (blank_row%2 == 1)
    
# MAIN()
input = []
initial_table = []
blank_row = 0
blank_col = 0

with open("config.txt") as fileIn:
    for line in fileIn:
        input.append(list(map(int, line.split())))

while input[0] != []:
    initial_table.append(input[0][:4])
    input[0] = input[0][4:]

while input[1] != []:
    FINAL_TABLE.append(input[1][:4])
    input[1] = input[1][4:]

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

last_num = -1
for i in range(len(FINAL_TABLE)):
    for j in range(len(FINAL_TABLE)):
        if(last_num>FINAL_TABLE[i][j] and FINAL_TABLE[i][j]!=0 and last_num!=0):
            NUM_INVERSIONS_FINAL+=1
        if(FINAL_TABLE[i][j] == 0):
            BLANK_ROW_FINAL = i
        last_num = FINAL_TABLE[i][j]

if(testSolvability(4 - blank_row,num_inversions) == (testSolvability(4 - BLANK_ROW_FINAL , NUM_INVERSIONS_FINAL))):
    
    initial_board = Board(initial_table, blank_row, blank_col)
    
    print("---------- STARTING DFS ----------\n")
    dfs = DFS(initial_board)
    if(dfs is not None):
        for i in dfs:
            print(str(i) + " =>" )
    print("---------- END OF DFS ----------\n")

    print("---------- STARTING IDFS ----------\n")
    idfs = IDFS(initial_board)
    for i in idfs:
        print(str(i) + " =>" )
    print("\n---------- END OF IDFS ----------\n")

    print("---------- STARTING BFS ----------\n")
    bfs, depthBfs, pathBfs = BFS(initial_board)
    if(bfs):
        for i in pathBfs:
            print(str(i) + " =>" )
        print("\n---------- SOLUTION FOUND ON DEPTH "+str(depthBfs)+" ----------")
    else:
        print("BFS DID NOT FIND ANY SOLUTION") 
    print("\n---------- END OF BFS ----------\n")  

    print("---------- STARTING A* MANHATTAN HEURISTIC ----------\n")
    astar_Man, depth_Man = A_star(initial_board, "MAN")
    if(astar_Man is not None):
        print("---------- SOLUTION FOUND ON DEPTH "+str(depth_Man)+" ----------")
        for i in astar_Man:
            print(str(i) + " =>" )
    else:
        print("---------- NO SOLUTION FOUND ----------\n")
    print("\n---------- END A* MANHATTAN HEURISTIC ----------\n")

    print("---------- STARTING A* SUM WRONG PLACES HEURISTIC ----------\n")
    astar_Sum , depth_Sum= A_star(initial_board, "SUM")
    if(astar_Sum is not None):
        print("---------- SOLUTION FOUND ON DEPTH "+str(depth_Sum)+" ----------")
        for i in astar_Sum:
            print(str(i) + " =>" )
    else:
        print("---------- NO SOLUTION FOUND ----------\n")
    print("\n---------- END A* SUM WRONG PLACES HEURISTIC ----------\n")
else:
    raise Exception("UNSOLVABLE BOARD: the initial configuration can't take you to the final configuration")


