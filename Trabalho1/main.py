from board import Board
from shared import FINAL_TABLE, BLANK_ROW_FINAL, NUM_INVERSIONS_FINAL
from depthFirstSearch import DFS
from iterativeDepthFirstSearch import IDFS
from breadthFirstSearch import BFS
from aStar import A_star
from greedy import greedy
import time

def testSolvability(blank_row, num_inversions):
    return (num_inversions%2 == 0) == (blank_row%2 == 1)
    
# MAIN()
tables = []
initial_table = []
blank_row = 0
blank_col = 0

with open("config.txt") as fileIn:
    for line in fileIn:
        tables.append(list(map(int, line.split())))

while tables[0] != []:
    initial_table.append(tables[0][:4])
    tables[0] = tables[0][4:]

while tables[1] != []:
    FINAL_TABLE.append(tables[1][:4])
    tables[1] = tables[1][4:]

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

    algorithm_to_run = int(input("Please input which algorithm you want to run:\n0: DFS\n1: IDFS\n2: BFS\n3: A*\n4: GREEDY\n"))
    total_time = 0
    total_memory = 0
    path = []

    match algorithm_to_run:
        case 0:
            print("---------- STARTING DFS ----------\n")
            start = time.time()
            dfs, num_nodes_gen, depth_dfs = DFS(initial_board)
            end = time.time()

            depth = depth_dfs
            path = dfs
            total_time = end - start
            total_memory = num_nodes_gen
        case 1:
            print("---------- STARTING IDFS ----------\n")
            start = time.time()
            idfs, num_nodes_gen, depth_idfs = IDFS(initial_board)
            end = time.time()

            depth = depth_idfs
            path = idfs
            total_time = end - start
            total_memory = num_nodes_gen
        case 2:
            print("---------- STARTING BFS ----------\n")
            start = time.time()
            bfs, depth_bfs, num_nodes_gen = BFS(initial_board)
            end = time.time()

            path = bfs
            depth = depth_bfs
            total_memory = num_nodes_gen
            total_time = end - start

        case 3:
            heu = int(input("\nWhich heuristic you want?\n0: Manhattan heuristic\n1: Sum of wrong places heuristic\n"))
            if(heu == 0):
                print("---------- STARTING A* MANHATTAN HEURISTIC ----------\n")
                start = time.time()
                astar_Man, depth_Astar_Man, num_nodes_gen = A_star(initial_board, "MAN")
                end = time.time()

                path = astar_Man
                depth = depth_Astar_Man
                total_memory = num_nodes_gen
                total_time = end - start
            else:
                print("---------- STARTING A* SUM WRONG PLACES HEURISTIC ----------\n")
                start = time.time()
                astar_Sum , depth_Astar_Sum, num_nodes_gen= A_star(initial_board, "SUM")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start

                path = astar_Sum
                depth = depth_Astar_Sum
                total_memory = num_nodes_gen
                total_time = end - start
        case 4:
            heu = int(input("\nWhich heuristic you want?\n0: Manhattan heuristic\n1: Sum of wrong places heuristic\n"))
            if(heu == 0):
                print("---------- STARTING GREEDY MANHATTAN HEURISTIC ----------\n")
                start = time.time()
                greedy_Man , depth_greedy_Man, num_nodes_gen = greedy(initial_board, "MAN")
                end = time.time()

                path = greedy_Man
                depth = depth_greedy_Man
                total_memory = num_nodes_gen
                total_time = end - start
            else:
                print("---------- STARTING GREEDY SUM WRONG PLACES HEURISTIC ----------\n")
                start = time.time()
                greedy_Sum , depth_greedy_Sum, num_nodes_gen = greedy(initial_board, "SUM")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start
                
                path = greedy_Sum
                depth = depth_greedy_Sum
                total_memory = num_nodes_gen
                total_time = end - start
        case _:
            print("NO ALGORITHM WAS CHOSEN, EXITING")
            exit()
    if(path is not None):
        print("SOLUTION FOUND\n")         
        print("TOTAL TIME SPENT: " + str(total_time))
        print("TOTAL MEMORY SPENT: " + str(total_memory))
        print("DEPTH OF SOLUTION: " + str(depth))
        x = input("Wuld u like to print the path taken?\n[Y]ES\n[N]O\n")
        if(x == 'Y' or x == 'y'):
            print("PATH TAKEN:")
            for i in path:
                print(str(i) + " =>" )
    else:
        print("NO SOLUTION FOUND")
else:
    raise Exception("UNSOLVABLE BOARD: the initial configuration can't take you to the final configuration")


